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
from pmp import views

urlpatterns = [
    url(r'^$', views.pmp_keywords_view, name='pmp'),
    url(r'^searchpmpkeywordslist', views.search_pmp_keywords_list, name='searchpmpkeywordslist'),
    url(r'^aboutview', views.about_view, name='aboutview'),
    url(r'^aboutlist', views.get_about_list, name='aboutlist'),
    url(r'^declareview', views.declare_view, name='declareview'),
    url(r'^declarelist', views.get_declare_list, name='declarelist'),

]
