from django.http.response import HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt
from wechart.models import WXDevInfo
import requests


@csrf_exempt
def check_signature(request):
    ' 微信接入操作 '
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'leartd'

        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print('[token, timestamp, nonce]', hashlist)
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')
        print('hashstr befor sha1', hashstr)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print('hashstr sha1', hashstr)
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('error')
    else:
        return HttpResponse('error')


AppId = WXDevInfo.objects.filter(id=1).values('AppId')
secret = WXDevInfo.objects.filter(id=1).values('AppSecret')
grant_type = 'client_credential'
baseUrl = 'https://api.weixin.qq.com/cgi-bin/'


def getAccessToken(request):
    ' 获取微信的accesstoken信息 '
    # token?grant_type = client_credential & appid = APPID & secret = APPSECRET
    url = baseUrl + 'token?grant_type = ' + grant_type + ' & appid =' + AppId + ' & secret = ' + secret
    response = requests.post(url=url)
    print(response)
    responsedata = response.json()
    # responsedata = {"access_token":"ACCESS_TOKEN","expires_in":7200}
    access_token = responsedata.get('access_token')
    return access_token


def joinUrl(menutype, action, accesstoken):
    ' 拼接url地址，menutype：菜单类型，如菜单menu；action：动作，如创建create；accesstoken：微信accesstoken'
    url = baseUrl + menutype + '/' + action + '/' + '?access_token=' + accesstoken
    return url


def gettextmessage(request):
    if request.method == 'POST':

        print(request.POST)
    return None



