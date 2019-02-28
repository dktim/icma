from django import forms
from case.models import TestCase

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        exclude = ("id",)

        widgets = {
          #  'name': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
          #  'idc': Select(attrs={'class': 'form-control', 'style': 'width:450px;'}),
           # 'desc': Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control', 'style': 'width:450px;'}),

        }
    
