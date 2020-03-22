from django.contrib import admin
from crm import models


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'referral', 'status')
    date_hierarchy = 'date'
    search_fields = ['name', ]
    list_filter = ['name', 'referral']
    list_editable = ['referral', 'status']


admin.site.register(models.Role)
admin.site.register(models.CourseList)
admin.site.register(models.Course)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.CourseRecord)
admin.site.register(models.CustomerFollow)
admin.site.register(models.UserProfile)
admin.site.register(models.Enrollment)
admin.site.register(models.StudyRecord)
admin.site.register(models.Tag)
admin.site.register(models.Menu)
