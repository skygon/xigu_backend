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

class Insurance(models.Model):
    name = models.CharField(max_length=128, verbose_name="保险名称")
    estimate_yearly_return = models.CharField(max_length=32, verbose_name="预计年化收益率")
    min_amount = models.CharField(max_length=32, verbose_name="起投金额", null=True, blank=True)
    invest_range = models.CharField(max_length=64, verbose_name="缴费期限", null=True, blank=True)


    class Meta:
        db_table = "insurance"
        verbose_name = '基金类产品'

    def __str__(self):
        return self.name


class Fund(models.Model):
    name = models.CharField(max_length=128, verbose_name="基金名称")
    estimate_yearly_return = models.CharField(max_length=32, verbose_name="预计年化收益率")
    history_yearly_return = models.CharField(max_length=32, verbose_name="历史平均年化收益率", null=True, blank=True)
    seven_day_return =  models.CharField(max_length=32, verbose_name="7日年化收益率")
    # 基金类产品字段
    min_amount = models.CharField(max_length=32, verbose_name="起投金额", null=True, blank=True)
    step_amount = models.CharField(max_length=32, verbose_name="递增金额", null=True, blank=True)
    # some projects may not have invest range property.
    invest_range = models.CharField(max_length=64, verbose_name="投资期限", null=True, blank=True)
    
    class Meta:
        db_table = "fund"
        verbose_name = '基金类产品'

    def __str__(self):
        return self.name


class RealEstate(models.Model):
    PROPERTY_TYPES = (('house','独栋别墅'),('apartmenet','公寓'), 
        ('townhouse','联排别墅'), ('multi-family house','多户住宅')
        )
    
    name = models.CharField(max_length=128, verbose_name="基金名称")
    estimate_yearly_return = models.CharField(max_length=32, verbose_name="预计年化收益率")

    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, verbose_name="房产类型",help_text="选择房产类型")
    bedrooms = models.CharField(max_length=64, verbose_name="卧室数量")
    sqft = models.CharField(max_length=64, verbose_name="使用面积")

    class Meta:
        db_table = "real_estate"
        verbose_name = '房产类产品'

    def __str__(self):
        return self.name

class CommercialEstate(models.Model):
    name = models.CharField(max_length=128, verbose_name="基金名称")
    estimate_yearly_return = models.CharField(max_length=32, verbose_name="预计年化收益率")

    total_price = models.CharField(max_length=64, verbose_name="项目总价")
    min_amount = models.CharField(max_length=32, verbose_name="起投金额", null=True, blank=True)
    invest_range = models.CharField(max_length=64, verbose_name="收益周期", null=True, blank=True)


    class Meta:
        db_table = "commercial_estate"
        verbose_name = '商业地产类产品'

    def __str__(self):
        return self.name

class Project(models.Model):
    TYPE = ((1, '基金'),(2, '房地产'),(3, '商业地产'), (4, '保险'))
    STATUS = ((1, '募集中'), (2, '已结束'))
    SHOW = ((0, '否'),(1, '是'))

    project_name = models.CharField(max_length=128, verbose_name="产品名称")
    project_type = models.IntegerField(choices=TYPE, verbose_name="产品类型")
    tags = models.CharField(max_length=128, verbose_name="产品标签", help_text="输入产品标签，以‘#’ 号分隔")
    project_status = models.IntegerField(default=1, choices=STATUS, verbose_name="产品状态")

    # 基金
    fund = models.OneToOneField(Fund, on_delete=models.CASCADE, null=True, blank=True, verbose_name="基金类产品")

    # 房地产
    real_estate = models.OneToOneField(RealEstate, on_delete=models.CASCADE, null=True, blank=True, verbose_name="房产类产品")

    # 商业地产
    commercial_estate = models.OneToOneField(CommercialEstate, on_delete=models.CASCADE, null=True, blank=True, verbose_name="商业地产类产品")

    # 保险
    insurance = models.OneToOneField(Insurance, on_delete=models.CASCADE, null=True, blank=True, verbose_name="保险类产品")

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