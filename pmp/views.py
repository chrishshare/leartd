from django.shortcuts import render
from favurls.views import get_session
from pmp.models import PMPDescription
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse


def pmp_keywords_view(request):
    if get_session(request) is not None:
        username = get_session(request).get('username')
    return render(request, 'pmp.html', locals())


def search_pmp_keywords_list(request):
    if request.method == 'GET':
        qryset = PMPDescription.objects.filter(version__contains='第六版').values('long_EN', 'short', 'long_CN', 'description', 'version')
        qryset.order_by('long_EN')
        result = json.dumps(list(qryset), cls=DjangoJSONEncoder, ensure_ascii=False)
        print(result)
        return HttpResponse(result)
    else:
        print(request.POST)
        option_value = request.POST.get('option_value')
        search_text = request.POST.get('search_text')
        if option_value == 'long_EN':
            qryset = PMPDescription.objects.filter(long_EN__contains=search_text, version__contains='第六版').values('long_EN', 'short', 'long_CN',
                                                                                         'description', 'version')
        elif option_value == 'short':
            qryset = PMPDescription.objects.filter(short=search_text, version__contains='第六版').values('long_EN', 'short', 'long_CN',
                                                                                         'description', 'version')
        elif option_value == 'long_CN':
            qryset = PMPDescription.objects.filter(long_CN__contains=search_text, version__contains='第六版').values('long_EN', 'short', 'long_CN',
                                                                             'description', 'version')
        else:
            qryset = PMPDescription.objects.filter(description__contains=search_text, version__contains='第六版').values('long_EN', 'short', 'long_CN',
                                                                               'description', 'version')
        qryset.order_by('long_EN')
        result = json.dumps(list(qryset), cls=DjangoJSONEncoder, ensure_ascii=False)
        print(result)
        return HttpResponse(result)


