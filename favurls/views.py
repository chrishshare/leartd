from django.shortcuts import render
from django.http import HttpResponse
from favurls.commonfunction import queryset_to_json, custominsert
from favurls.models import UrlManager, UrlClassify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.core.serializers.json import DjangoJSONEncoder


def index_view(request):
    """ 首页渲染，必须登陆才能查询url信息，否则提示需要登陆，默认显示广告(o^o) """
    if get_session(request) is not None:
        username = get_session(request).get('username')
    # classify_list = get_url_classify(request)
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def get_url_classify(request):
    """ 获取当前登陆用户的url分类 """
    if get_session(request) is not None:
        result = UrlClassify.objects.all().values('type_code', 'type_name')
        json_data = queryset_to_json(result)
        return HttpResponse(json_data)
    else:
        pass


@login_required(login_url='/accounts/login/')
def search_user_urls(request):
    if get_session(request) is not None:
        if request.method == 'POST':
            username = get_session(request).get('username')
            url_name = request.POST.get('url-name')
            type_code = request.POST.get('type-code')

            if len(request.POST.get('type-code')) == 0:
                result = UrlManager.objects.filter(creator__username=username,
                                                   url_name__contains=url_name).values(
                    'url_name',
                    'url_link',
                    'classify__type_code',
                    'classify__type_name',
                    'note')
            else:
                result = UrlManager.objects.filter(creator__username=username,
                                                   url_name__contains=url_name,
                                                   classify__type_code=type_code).values(
                    'url_name',
                    'url_link',
                    'classify__type_code',
                    'classify__type_name',
                    'note')

            result.order_by('classify__type_code')
            json_data = queryset_to_json(result)
        else:

            result = UrlManager.objects.filter(creator__username=get_session(request).get('username')).values(
                'url_name',
                'url_link',
                'classify__type_code',
                'classify__type_name',
                'note')

            result.order_by('classify__type_code')
            json_data = queryset_to_json(result)
        return HttpResponse(json_data)
    else:
        pass


def add_url(request):
    if get_session(request) is not None:
        if request.method == 'POST':
            print('addurl post:', request.POST)
            url_link = request.POST.get('urllink')
            url_name = request.POST.get('urlname')
            classify_id = request.POST.get('urltype')
            type_code = UrlClassify.objects.get(type_code=classify_id)
            remark = request.POST.get('remark')
            user = User.objects.get(username=get_session(request).get('username'))
            # createtime = now()

            try:
                UrlManager.objects.create(url_name=url_name, url_link=url_link, note=remark,
                                          classify=type_code, creator=user)
                result = json.dumps([{'message_code': '0', 'messages': 'URL增加成功'}], cls=DjangoJSONEncoder, ensure_ascii=False)
            except:
                result = json.dumps([{'message_code': '-1', 'messages': 'URL增加失败'}], cls=DjangoJSONEncoder, ensure_ascii=False)
            print(result)
            return HttpResponse(result)


def add_classify(request):
    if get_session(request) is not None:
        if request.method == 'POST':
            type_code = request.POST.get('typecode')
            type_name = request.POST.get('typename')
            user = User.objects.get(username=get_session(request).get('username'))
            # createtime = now()

            try:
                UrlClassify.objects.create(type_code=type_code, type_name=type_name, creator=user)
                result = json.dumps([{'message_code': '0', 'messages': 'URL分类增加成功'}], cls=DjangoJSONEncoder, ensure_ascii=False)
            except:
                result = json.dumps([{'message_code': '-1', 'messages': 'URL分类增加失败'}], cls=DjangoJSONEncoder, ensure_ascii=False)
            print(result)
            return HttpResponse(result)


def get_session(request):
    """ 获取session，如果成功，则返回id，username字典，否则返回None """
    if '_auth_user_id' in request.session:
        userid = request.session.get('_auth_user_id')
        username = User.objects.filter(id=userid).values('username')[0]['username']
        return {'id': id, 'username': username}
    else:
        return None
