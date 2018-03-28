from django.http.response import HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt
from wechart.models import WXDevInfo
import requests
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message, create_reply
from wechatpy.client.api import menu
from wechatpy import WeChatClient

#
# @csrf_exempt
# def check_signature(request):
#     ' 微信接入操作 '
#     if request.method == 'GET':
#         signature = request.GET.get('signature')
#         timestamp = request.GET.get('timestamp')
#         nonce = request.GET.get('nonce')
#         echostr = request.GET.get('echostr')
#         token = 'leartd'
#
#         hashlist = [token, timestamp, nonce]
#         hashlist.sort()
#         print('[token, timestamp, nonce]', hashlist)
#         hashstr = ''.join([s for s in hashlist]).encode('utf-8')
#         print('hashstr befor sha1', hashstr)
#         hashstr = hashlib.sha1(hashstr).hexdigest()
#         print('hashstr sha1', hashstr)
#         if hashstr == signature:
#             return HttpResponse(echostr)
#         else:
#             return HttpResponse('error')
#     else:
#         return HttpResponse('error')


TOKEN = 'leartd'


@csrf_exempt
def wei_xin(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echo_str = request.GET.get('echostr')
        try:
            check_signature(token=TOKEN, signature=signature, timestamp=timestamp, nonce=nonce)
        except InvalidSignatureException:
            echo_str = 'error'
        response = HttpResponse(echo_str, content_type='text/plain')
        return response
    elif request.method == 'POST':
        msg = parse_message(request.body)
        if msg.type == 'text' and msg.content == 'aini':
            reply = create_reply('http://blog.csdn.net/zhangpp12321/article/details/72639308', msg)
        elif msg.type == 'image':
            reply = create_reply('image', msg)
        elif msg.type == 'voice':
            reply = create_reply('voice', msg)
        else:
            reply = create_reply('other', msg)
        response = HttpResponse(reply.render(), content_type='application/xml')
        return response
    else:
        pass


AppId = WXDevInfo.objects.filter(id=1).values('AppId')
secret = WXDevInfo.objects.filter(id=1).values('AppSecret')
grant_type = 'client_credential'
baseUrl = 'https://api.weixin.qq.com/cgi-bin/'


def getAccessToken(request):
    print(request.method)
    ' 获取微信的accesstoken信息 '
    # token?grant_type = client_credential & appid = APPID & secret = APPSECRET
    url = baseUrl + 'token?grant_type = ' + grant_type + ' & appid =' + AppId + ' & secret = ' + secret
    response = requests.post(url=url)
    print(response)
    responsedata = response.json()
    # responsedata = {"access_token":"ACCESS_TOKEN","expires_in":7200}
    access_token = responsedata.get('access_token')
    return access_token


def access_url(menutype, action, accesstoken):
    ' 拼接url地址，menutype：菜单类型，如菜单menu；action：动作，如创建create；accesstoken：微信accesstoken'
    url = baseUrl + menutype + '/' + action + '/' + '?access_token=' + accesstoken
    return url


def reply_message(request):
    msg = parse_message(request.body)
    if msg.type == 'text':
        reply = create_reply('wenzi', msg)
    elif msg.type == 'image':
        reply = create_reply('image', msg)
    elif msg.type == 'voice':
        reply = create_reply('voice', msg)
    else:
        reply = create_reply('other', msg)
    response = HttpResponse(reply.render(), content_type='application/xml')
    return response


def create_menu(request):
    client = WeChatClient('appid', 'secret')
    client.menu.add_conditional({
             "button":[
             {
                  "type":"click",
                  "name":"今日歌曲",
                  "key":"V1001_TODAY_MUSIC"
              },
              {
                   "name":"菜单",
                   "sub_button":[
                   {
                       "type":"view",
                       "name":"搜索",
                       "url":"http://www.soso.com/"
                    },
                    {
                         "type":"miniprogram",
                         "name":"wxa",
                         "url":"http://mp.weixin.qq.com",
                         "appid":"wx286b93c14bbf93aa",
                         "pagepath":"pages/lunar/index"
                     },
                    {
                       "type":"click",
                       "name":"赞一下我们",
                       "key":"V1001_GOOD"
                    }]
               }]
         })
