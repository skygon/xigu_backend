from django.contrib import admin
from .models import Investment
# Register your models here.


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'principal', 'interest', 'unit', 'user', 'project')


admin.site.register(Investment, InvestmentAdmin)