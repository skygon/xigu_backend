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
    STATUS = ((1, '募集中'), (2, '已结束'))
    SHOW = ((0, '否'),(1, '是'))

    project_name = models.CharField(max_length=128, verbose_name="产品名称")
    project_type = models.IntegerField(choise=TYPE, verbose_name="产品类型")
    estimate_yearly_return = models.CharField(max_length=32, verbose_name="预计年化收益率")
    history_yearly_return = models.CharField(max_length=32, verbose_name="历史平均年化收益率", null=True, blank=True)

    project_status = models.IntegerField(default=1, choise=STATUS, verbose_name="产品状态")
    # 基金类产品字段
    min_amount = models.CharField(max_length=32, verbose_name="起投金额", null=True, blank=True)
    step_amount = models.CharField(max_length=32, verbose_name="递增金额", null=True, blank=True)
    # some projects may not have invest range property.
    invest_range = models.CharField(max_length=64, verbose_name="投资期限", null=True, blank=True)

    project_detail = models.OneToOneField(ProjectDescription, on_delete=models.CASCADE, null=True, blank=True, verbose_name="产品详细描述")

    #是否需要在项目列表中显示
    is_show = models.IntegerField(choices=SHOW, default=1, verbose_name="是显示该产品")

    # 置顶
    is_top = models.IntegerField(default=0, verbose_name="是否置顶", help_text="设置大于0的数表示置顶，数字越大优先级越高")
    
    class Meta:
        db_table = "project"
        verbose_name = '产品'

    def __str__(self):
        return self.project_name