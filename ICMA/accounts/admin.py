from django.contrib import admin
from case.models import TestCase,productionUser
from project.models import Project,task,subtask

admin.site.register(TestCase)
admin.site.register(productionUser)
admin.site.register(Project)
admin.site.register(task)
admin.site.register(subtask)
