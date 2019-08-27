from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #针对显示列表的更改,在列表中显示投票信息
    list_display = ('question_text','pub_date','was_published_recently')

    #针对字段的排序，类型等更改。
    fieldsets = [(None, {'fields':['question_text']}),
                ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
              ]
    #显示外键相关联内容
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
