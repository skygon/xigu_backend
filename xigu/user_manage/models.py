from django.db import models
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from project.models import Project

# Create your models here.
class User(models.Model):
    GENDER = ((0, "不详"), (1, "男"), (2, "女"))

    name = models.CharField(max_length=32, null=True, blank=True, verbose_name="姓名")
    gender = models.IntegerField(default=0, choices=GENDER, null=True, blank=True, verbose_name="性别")
    mobile = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="手机号")
    
    # 用户预约产品
    follow_projects = models.ManyToManyField(Project, verbose_name="预约产品")
    
    register_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='注册时间')
    last_active_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="最近活跃时间")
    
    def __str__(self):
        return self.mobile
    
    class Meta:
        db_table = "user"
        verbose_name = '用户表'