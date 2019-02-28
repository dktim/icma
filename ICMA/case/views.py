from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify
from case.models import TestCase
from django.http.response import HttpResponse
from case.forms import TestCaseForm
from ICMA.api import get_object
# Create your views here.
@login_required()
@permission_verify()
def test_case_list(request):
    testcase_info=TestCase.objects.filter(charge_user=request.user.id).all()
    print 
    temp_name = "headers/testcase-header.html"  
    dd={}
    return render_to_response('testcase/testcase.html', locals())


@login_required()
@permission_verify()
def change_case_status(request,case_id,handle_type):
    if type=='success':
        pass
    
    
    return HttpResponse() 


def test_case_edit(request,id):
    temp_name = "headers/testcase-header.html"  
    obj = get_object(TestCase, id=id)
    if request.method == 'POST':
        form = TestCaseForm(request.POST, instance=obj)
        if form.is_valid():
            try:
                form.save()
                status = 1
            except:
                status = 2
        else:
            status = 2
    else:
        form = TestCaseForm(instance=obj)
    return render(request, "testcase/testcase_edit.html", locals())


