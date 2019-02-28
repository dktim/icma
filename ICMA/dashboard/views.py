#coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
from project.models import Project,task,subtask
from django.http.response import HttpResponse, JsonResponse
import project
import json
# Create your views here.

from project.models import SUBTASK_STATUS
from django.db.models import Q

def dashboard(request,p_id):
    project=Project.objects.get(id=p_id)
    project_name=project.p_name
    
    tasks_obj=task.objects.filter(project=project)
    tasks=[]
    for t in tasks_obj:
     
    
        tasks.append(t)
        print t.status


    temp_name='main-header.html'
    ret={
    'p_name':project_name,
    'tasks':tasks,
    'p_id':p_id
    }
    return render(request,'dashboard/index.html',locals())


"""
var data = [
                        {id: '1', name: '预投产准备', status: '2'},
                        {id: '2', name: '投产准备', status: '2'},
                        {id: '3', name: '投产', status: '3'},
                        {id: '4', name: '测试', status: '1'},
                        {id: '5', name: '扫码付验证', status: '1'},
                        {id: '6', name: '总结', status: '0'},
                        {id: '7', name: '总结2', status: '0'},
                        {id: '8', name: '总结3', status: '0'}
                    ];*/
"""

def dashboard_task_list(request,p_id):
    tasks_obj=task.objects.filter(project_id=p_id)
    
    data=[]
    for task_obj in tasks_obj:
        ret={
        'id':task_obj.id,
        'name':task_obj.task_name,
        
        'status':task_obj.status
        }
        print task_obj.task_name
        data.append(ret)
    print data
    #return JsonResponse(json.dumps(data),safe=False,ensure_ascii=False,content_type='application/json,charset=utf-8')
    return JsonResponse(json.dumps(data),safe=False,content_type='application/json,charset=utf-8')   
    



def dashboard_subtask_list(request,task_id):
    task_objs=task.objects.get(id=task_id)
    #print task_objs
    subtasks=subtask.objects.filter(task=task_objs)

   # subtasks=task_objs.sub_task.all()
    print subtasks
   
    ret_dict={}
    substep=[]
    for sub in subtasks:
        substep.append(
            {'name':sub.content,
            'status':sub.status
            }
            )

    ret_dict={
        'substep':substep,
        'charge_user':task_objs.charge_user.username,
        'execute_user':task_objs.execute_user.username,
        'start_time':task_objs.start_time,
        'end_time':task_objs.end_time
    }
    print json.dumps(ret_dict)

  
    return JsonResponse(ret_dict,safe=False)   

def test_case_edit(request,id):
    pass
    
    
def my_task(request):
    temp_name='headers/my-header.html'
    projects = Project.objects.all()
    audit_status = SUBTASK_STATUS
    project_name = request.GET.get('project', '')
    status = request.GET.get('status', '')
    keyword = request.GET.get('keyword', '')

    print 'project_name:',project_name
    my_subtask=subtask.objects.filter(charge_user=request.user.id).order_by('-id')
   # if project_name:
  #      my_subtask = my_subtask.filter(project__p_name__contains=project_name)
    if status:
        my_subtask = my_subtask.filter(status=status)
    if keyword:
        my_subtask = my_subtask.filter(Q(content__contains=keyword))
    print '[[[[[]]]].',my_subtask
    return render(request,'dashboard/my_dashboard.html',locals())


def my_test(request):
    temp_name = 'headers/my-header.html'
  #  projects = Project.objects.all()
  #  audit_status = SUBTASK_STATUS
    project_name = request.GET.get('project', '')
    status = request.GET.get('status', '')
    keyword = request.GET.get('keyword', '')
    pass