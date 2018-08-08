from django.db import models
from DjangoUeditor.models import UEditorField
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from xigu_utils.model_util import BaseImage, AliyunStorage
#from photos.models import Photo


class Image(BaseImage):
    class Meta:
        verbose_name = '图片'
        db_table = 'image' 


class ProjectDescription(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    #content = RichTextUploadingField(blank=True, null=True, verbose_name="内容")
    content = UEditorField(u'内容	', toolbars="full", imagePath="upload/", filePath="", upload_settings={"imageMaxSize":20480000}, settings={},command=None,blank=True) # imageMaxSize 20 MB

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "project_desc"
        verbose_name = '产品描述'


class Project(models.Model):
    TYPE = ((1, '基金'),(2, '保险'),(3, '商业地产'))

    project_name = models.CharField(max_length=128, verbose_name="产品名称")
    project_type = models.IntegerField(choise=TYPE, verbose_name="产品类型")
    estimate_yearly_return = models.CharField(max_length=32, verbose_name="预计年化收益率")
    invest_range = models.CharField(max_length=64, verbose_name="投资期限")

    # 基金类产品字段
    class Meta:
        db_table = "project"
        verbose_name = '产品'

    def __str__(self):
        return self.project_name