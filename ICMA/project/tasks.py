#coding:utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from project.models import Project,task
from django.shortcuts import render_to_response
from project.forms import TaskForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify

from project.models import  task
from project.forms import TaskForm
from ICMA.api import get_object
@login_required()
@permission_verify()
def task_list(request):
    current_project=Project.objects.get(is_current=1)
    print current_project
    task_info = current_project.project_task.all()

    temp_name = "headers/project-header.html"
    dd={}
    return render_to_response('task/task.html', locals())
    

def task_add(request):
    temp_name = "headers/project-header.html"
    if request.method == "POST":
        print "post"
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render(request, "task/task_add.html", locals())
    else:
        print "get"
        display_control = "none"
        task_form = TaskForm()
        return render(request, "task/task_add.html", locals())


def task_edit(request,id):
    temp_name = "headers/testcase-header.html"
    obj = get_object(task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj)
        print form.is_valid()
        if form.is_valid():
            try:
                form.save()
                status = 1
            except:
                status = 2
        else:
            status = 2
        print status
    else:
        form = TaskForm(instance=obj)


    return render(request, "task/task_edit.html", locals())

def task_del(request):
    pass
