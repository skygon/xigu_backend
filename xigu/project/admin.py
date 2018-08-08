from django.contrib import admin
from .models import Project
from .models import ProjectDescription
from .models import Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from xigu_utils import utils

def preview(self):
    return mark_safe(u'<img src="%s?x-oss-process=style/mini_thumbnail" height="64" width="64" />' %(self.img.url))
preview.allow_tags = True
preview.short_description = "preview"

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'create_time')
    #fields = ('name', 'img',  'image_tag',)
    #readonly_fields = ('create_time','image_tag',)
  
#admin.site.register(Image, ImageAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_type', 'estimate_yearly_return', 'history_yearly_return', 'project_status', 'min_amount', 'step_amount', 'invest_range', 'is_show', 'is_top')

    #filter_horizontal = ('detail_photos', 'layout_photos', )


#admin.site.register(Project)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDescription)
admin.site.register(Image, ImageAdmin)