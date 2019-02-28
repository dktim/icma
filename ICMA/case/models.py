#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from accounts.models import UserInfo
from project.models import Project

# Create your models here.

class productionUser(models.Model):
    name = models.CharField(u"负责人姓名", max_length=50, unique=True, null=False, blank=False)
    phone = models.CharField(u"负责人手机", max_length=50, null=False, blank=False)
    qq = models.CharField(u"负责人QQ", max_length=100, null=True, blank=True)
    weChat = models.CharField(u"负责人微信", max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

TEST_CASE_STATUS=(
    (str(0),u'成功',),
    (str(1),u'失败',),
  
    )
class TestCase(models.Model):
    project_own=models.ForeignKey(Project,null=True,verbose_name=u'测试案例所属项目',blank=True)
    testcase_name=models.CharField(u'案例名称',max_length=128)
    testcase_content=models.CharField(u'案例描述',max_length=128)
    charge_user=models.ForeignKey(UserInfo,verbose_name=u'anli负责人')
    status = models.CharField(u"测试任务状态", choices=TEST_CASE_STATUS, max_length=30, null=True, blank=True)
    

