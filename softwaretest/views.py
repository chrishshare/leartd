from django.shortcuts import render
from favurls.views import get_session
from softwaretest.models import SoftwareTest
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse


def software_test_keywords_view(request):
    if get_session(request) is not None:
        username = get_session(request).get('username')
    return render(request, 'softwaretest.html', locals())


def search_software_test_keywords_list(request):
    if request.method == 'GET':
        qryset = SoftwareTest.objects.values('long_EN', 'short', 'long_CN', 'description', 'keyword')
        qryset.order_by('long_EN')
        result = json.dumps(list(qryset), cls=DjangoJSONEncoder, ensure_ascii=False)
        print(result)
        return HttpResponse(result)
    else:
        print(request.POST)
        option_value = request.POST.get('option_value')
        search_text = request.POST.get('search_text')
        if option_value == 'long_EN':
            qryset = SoftwareTest.objects.filter(long_EN__contains=search_text).values('long_EN', 'short', 'long_CN',
                                                                                         'description', 'keyword')
        elif option_value == 'short':
            qryset = SoftwareTest.objects.filter(short=search_text).values('long_EN', 'short', 'long_CN',
                                                                                         'description', 'keyword')
        elif option_value == 'long_CN':
            qryset = SoftwareTest.objects.filter(long_CN__contains=search_text).values('long_EN', 'short', 'long_CN',
                                                                             'description', 'keyword')
        else:
            qryset = SoftwareTest.objects.filter(description__contains=search_text).values('long_EN', 'short', 'long_CN',
                                                                               'description', 'keyword')
        qryset.order_by('long_EN')
        result = json.dumps(list(qryset), cls=DjangoJSONEncoder, ensure_ascii=False)
        print(result)
        return HttpResponse(result)


