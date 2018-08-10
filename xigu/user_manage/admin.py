from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'register_time', 'last_active_time')
    filter_horizontal = ('follow_projects', )


admin.site.register(User, UserAdmin)