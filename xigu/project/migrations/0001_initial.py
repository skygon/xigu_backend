# Generated by Django 2.0.4 on 2018-08-13 05:38

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion
import xigu_utils.model_util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommercialEstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='基金名称')),
                ('estimate_yearly_return', models.CharField(max_length=32, verbose_name='预计年化收益率')),
                ('total_price', models.CharField(max_length=64, verbose_name='项目总价')),
                ('min_amount', models.CharField(blank=True, max_length=32, null=True, verbose_name='起投金额')),
                ('invest_range', models.CharField(blank=True, max_length=64, null=True, verbose_name='收益周期')),
            ],
            options={
                'db_table': 'commercial_estate',
                'verbose_name': '商业地产类产品',
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='基金名称')),
                ('estimate_yearly_return', models.CharField(max_length=32, verbose_name='预计年化收益率')),
                ('history_yearly_return', models.CharField(blank=True, max_length=32, null=True, verbose_name='历史平均年化收益率')),
                ('seven_day_return', models.CharField(max_length=32, verbose_name='7日年化收益率')),
                ('min_amount', models.CharField(blank=True, max_length=32, null=True, verbose_name='起投金额')),
                ('step_amount', models.CharField(blank=True, max_length=32, null=True, verbose_name='递增金额')),
                ('invest_range', models.CharField(blank=True, max_length=64, null=True, verbose_name='投资期限')),
            ],
            options={
                'db_table': 'fund',
                'verbose_name': '基金类产品',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='名称')),
                ('img', models.ImageField(storage=xigu_utils.model_util.AliyunStorage(), upload_to='', verbose_name='URL')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'image',
                'verbose_name': '图片',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='保险名称')),
                ('estimate_yearly_return', models.CharField(max_length=32, verbose_name='预计年化收益率')),
                ('min_amount', models.CharField(blank=True, max_length=32, null=True, verbose_name='起投金额')),
                ('invest_range', models.CharField(blank=True, max_length=64, null=True, verbose_name='缴费期限')),
                ('age_range', models.CharField(max_length=64, verbose_name='投保年龄')),
            ],
            options={
                'db_table': 'insurance',
                'verbose_name': '保险类产品',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128, verbose_name='产品名称')),
                ('project_type', models.IntegerField(choices=[(1, '基金'), (2, '房地产'), (3, '商业地产'), (4, '保险')], verbose_name='产品类型')),
                ('tags', models.CharField(help_text='输入产品标签，以‘#’ 号分隔', max_length=128, verbose_name='产品标签')),
                ('project_status', models.IntegerField(choices=[(1, '募集中'), (2, '已结束')], default=1, verbose_name='产品状态')),
                ('is_show', models.IntegerField(choices=[(0, '否'), (1, '是')], default=1, verbose_name='是显示该产品')),
                ('is_top', models.IntegerField(default=0, help_text='设置大于0的数表示置顶，数字越大优先级越高', verbose_name='是否置顶')),
                ('commercial_estate', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.CommercialEstate', verbose_name='商业地产类产品')),
                ('fund', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Fund', verbose_name='基金类产品')),
                ('insurance', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Insurance', verbose_name='保险类产品')),
            ],
            options={
                'db_table': 'project',
                'verbose_name': '产品',
            },
        ),
        migrations.CreateModel(
            name='ProjectDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容\t')),
            ],
            options={
                'db_table': 'project_desc',
                'verbose_name': '产品描述',
            },
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='基金名称')),
                ('estimate_yearly_return', models.CharField(max_length=32, verbose_name='预计年化收益率')),
                ('property_type', models.CharField(choices=[('house', '独栋别墅'), ('apartmenet', '公寓'), ('townhouse', '联排别墅'), ('multi-family house', '多户住宅')], help_text='选择房产类型', max_length=50, verbose_name='房产类型')),
                ('bedrooms', models.CharField(max_length=64, verbose_name='卧室数量')),
                ('sqft', models.CharField(max_length=64, verbose_name='使用面积')),
            ],
            options={
                'db_table': 'real_estate',
                'verbose_name': '房产类产品',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectDescription', verbose_name='产品详细描述'),
        ),
        migrations.AddField(
            model_name='project',
            name='real_estate',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.RealEstate', verbose_name='房产类产品'),
        ),
    ]
