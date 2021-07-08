from django.contrib import admin

# Register your models here.
from login.models import SiteUser
class SiteUserAdmin(admin.ModelAdmin):
    list_display=['name','gender','email']
    list_display_links=['name']
    list_filter=['gender','create_time']   #通过性别或者创建时间进行筛选

admin.site.register(SiteUser,SiteUserAdmin)   #将git SiteUserAdmin绑定到SiteUser