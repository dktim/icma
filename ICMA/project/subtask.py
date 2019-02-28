#coding:utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from project.models import Project,task,subtask
from django.shortcuts import render_to_response
from project.forms import TaskForm, subTaskForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify
from ICMA.api import get_object
@login_required()
@permission_verify()
def subtask_list(request):
    subtaskinfo=subtask.objects.all()
    temp_name = "headers/project-header.html"  
    dd={}
    return render_to_response('subtask/subtask.html', locals())
    
@login_required()
@permission_verify()
def subtask_add(request):
    temp_name = "headers/project-header.html"
    if request.method == "POST":
        print "post"
        subtask_form = subTaskForm(request.POST)
        if subtask_form.is_valid():
            subtask_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render(request, "subtask/subtask_add.html", locals())
    else:
        print "get"
        display_control = "none"
        subtask_form = subTaskForm()
        return render(request, "subtask/subtask_add.html", locals())
@login_required()
@permission_verify()
def subtask_del(request):
    pass


def subtask_edit(request,id):
    temp_name = "headers/testcase-header.html"
    obj = get_object(subtask, id=id)
    if request.method == 'POST':
        form = subTaskForm(request.POST, instance=obj)
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
        form = subTaskForm(instance=obj)


    return render(request, "subtask/subtask_edit.html", locals())