from django.db import models
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from project.models import Project
from user_manage.models import User

# Create your models here.
class Investment(models.Model):
    UNIT = ((0, '人民币'), (1, '美元'))

    name = models.CharField(max_length=64, verbose_name='名称')

    principal = models.DecimalField(default=0, max_digits=11, decimal_places=2, verbose_name='本金')
    interest = models.DecimalField(default=0, max_digits=11, decimal_places=2, verbose_name='收益')
    unit = models.IntegerField(choices=UNIT, default=0, verbose_name="资产单位")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "investment"
        verbose_name = '投资表'