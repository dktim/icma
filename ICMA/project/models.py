#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from accounts.models import UserInfo

# Create your models here.


TASK_STATUS=(
    (str(0),u'未开始'),
    (str(1),u'执行中',),
    (str(2),u'执行成功',),
      (str(3),u'执行失败',),
    )

SUBTASK_STATUS=(
    
    (str(0),u'未开始'),
    (str(1),u'成功',),
     (str(2),u'失败',),
    )


class Project(models.Model):
    is_current=models.IntegerField(u'是否当前项目',blank=True,null=True)
    p_name=models.CharField(verbose_name=u'项目名称',max_length=40,unique=True)
    p_desc=models.CharField(verbose_name=u'项目描述',max_length=40,unique=True)
   # img_path=models.ImageField("项目背景图",null=True,upload_to='project_img/')
    def __unicode__(self):
        return self.p_name
    class meta():
        verbose_name = u'项目名称'
        verbose_name_plural = verbose_name


class task(models.Model):
    project = models.ForeignKey(Project, verbose_name='所属项目', related_name='project_task', blank=True, null=True)
    t_id = models.IntegerField(u't_id', blank=True, null=True)
    task_name = models.CharField(verbose_name=u'任务名称', max_length=64)
    task_content = models.TextField(u'任务内容', max_length=255, blank=True)
    expect_time = models.IntegerField(u'预计需要时间', blank=True, null=True)
    execute_user = models.ForeignKey(UserInfo, related_name='execute_user', verbose_name=u'执行人')
    status = models.CharField(u"任务状态", choices=TASK_STATUS, max_length=30, null=True, blank=True, default=0)
    charge_user = models.ForeignKey(UserInfo, verbose_name=u'责任人', related_name='charge_user')
    pic = models.ImageField(u'步骤图', null=True, upload_to='task_img/', blank=True)
    # sub_task=models.ManyToManyField(subtask)
    start_time = models.CharField(verbose_name=u'开始时间', max_length=250, null=True, blank=True)
    end_time = models.CharField(verbose_name=u'结束时间', max_length=250, null=True, blank=True)

    #  sub_task=models.ManyToManyField(subtask,verbose_name=u'子任务')
    # sub_task=models.CharField(u'子任务描述',max_length=256,null=True,blank=True)
    def __unicode__(self):
        return self.task_name


class subtask(models.Model):
    task=models.ForeignKey(task,verbose_name='所属任务',default='')
    content=models.CharField(u'子任务描述',max_length=250)
    charge_user=models.ForeignKey(UserInfo,verbose_name=u'责任人',related_name='subtask_charge_user',null=True,blank=True)
    status = models.CharField(u"子任务状态", choices=SUBTASK_STATUS, max_length=30, null=True, blank=True)
    
    def __unicode__(self):
        return self.content


    
if __name__ == '__main__':
    pass
    
    
    
