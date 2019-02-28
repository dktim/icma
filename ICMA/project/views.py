#coding:utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from project.models import Project,task
from django.shortcuts import render_to_response
from project.forms import ProjectForm
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify
# Create your views here.

@login_required()
@permission_verify()
def project_list(request):
    project_info=Project.objects.all()
    temp_name = "headers/project-header.html"  
    dd={}
    return render_to_response('project/project.html', locals())
    
@login_required()
@permission_verify()
def project_add(request):
    temp_name = "headers/project-header.html"
    if request.method == "POST":
        print "post"
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render(request, "project/project_add.html", locals())
    else:
        print "get"
        display_control = "none"
        project_form = ProjectForm()
        return render(request, "project/project_add.html", locals())
    
    
    
@login_required()
@permission_verify()
def project_edit(request):
    pass
@login_required()
@permission_verify()
def project_del(request):
    pass


@login_required()
@permission_verify()
def project_distribute(request):
    pass

def project_task_list(request,ids):
    project_info=Project.objects.get(id=ids)
    project_name=project_info.p_name
    task_info=task.objects.filter(project=ids)
    print task_info

    return render(request, "project/project_task_list.html", locals())