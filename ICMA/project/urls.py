#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from accounts import user, role, permission
from project.views import *

from project import tasks as tasks_views
from project import subtask as subtask_views


urlpatterns = [
   
   url(r'^project/list/$', project_list, name='project_list'),
url(r'^project_task/list/(?P<ids>\d+)/$', project_task_list, name='project_task_list'),
   url(r'^project/add/$',   project_add, name='project_add'),
   url(r'^project/delete/(?P<ids>\d+)/$',  project_del, name='project_del'),

  url(r'^task/list/$', tasks_views.task_list, name='task_list'),
   url(r'^task/add/$',   tasks_views.task_add, name='task_add'),
   url(r'^task/delete/(?P<ids>\d+)/$', tasks_views.task_del, name='task_del'),
url(r'^task/edit/(?P<id>\d+)/$',tasks_views.task_edit,name='task_edit'),
   
    url(r'^subtask/list/$', subtask_views.subtask_list, name='subtask_list'),
   url(r'^subtask/add/$',   subtask_views.subtask_add, name='subtask_add'),
   url(r'^subtask/delete/(?P<ids>\d+)/$', subtask_views.subtask_del, name='subtask_del'),
url(r'^subtask/edit/(?P<id>\d+)/$',subtask_views.subtask_edit,name='subtask_edit'),

    url(r'^project/distribute/',  project_distribute, name='project_distribute'),
]
