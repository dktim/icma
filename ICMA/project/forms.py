from project.models import Project,task,subtask
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ("id", )

        widgets = {
          #  'name': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
          #  'idc': Select(attrs={'class': 'form-control', 'style': 'width:450px;'}),
           # 'desc': Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control', 'style': 'width:450px;'}),

        }
    

class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        exclude = ("id", 'pic','t_id',)

        widgets = {
          #  'name': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
          #  'idc': Select(attrs={'class': 'form-control', 'style': 'width:450px;'}),
           # 'desc': Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control', 'style': 'width:450px;'}),

        }
        
        
class subTaskForm(forms.ModelForm):
    class Meta:
        model = subtask
        exclude = ("id",)

        widgets = {
          #  'name': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
          #  'idc': Select(attrs={'class': 'form-control', 'style': 'width:450px;'}),
           # 'desc': Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control', 'style': 'width:450px;'}),

        }