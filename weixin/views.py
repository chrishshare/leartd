from django.shortcuts import render
from django.http.response import HttpResponse
import hashlib
TOKEN = "leartd"

# Create your views here.


def checkSignature(request):
    token = '自己随意写'
    signature = request.GET.get('signature', '')
    timestamp = request.GET.get('timestamp', '')
    nonce = request.GET.get('nonce',  '')
    echostr = request.GET.get('echostr', '')

    infostr = ''.join(sorted([token, timestamp, nonce]))
    if infostr:
        hashstr = hashlib.sha1(infostr).hexdigest()
        if hashstr is signature:
            return HttpResponse(echostr)
        else:
            print('haststr is not signature')
    else:
        print('infostr does not existing')

