"""leartd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from favurls import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^urlmanager', views.url_manager_view, name='urlmanager'),
    url(r'^getclassify/$', views.get_url_classify, name='getclassify'),
    url(r'^geturls', views.search_user_urls, name='geturls'),
    url(r'^addurl', views.add_url, name='addurl'),
    url(r'^addclassify', views.add_classify, name='addclassify'),
    url(r'^delurl', views.del_url, name='delurl'),
    url(r'^delclassify', views.del_classify, name='delclassify'),
]
