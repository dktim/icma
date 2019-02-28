"""ICMA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from case.views import test_case_list,change_case_status,test_case_edit

urlpatterns = [
     
   # url(r'^$',views.index,name='xx'),
    url(r'^case/list/$',test_case_list,name='case'),
    url(r'^case/edit/(?P<id>\d+)/$',test_case_edit,name='test_case_edit'),
    url(r'^change_case_status/$',change_case_status,name='change_case_status'),
 
 
]
