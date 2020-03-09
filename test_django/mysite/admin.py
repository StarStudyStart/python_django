from django.contrib import admin
from mysite.models import Author, Book, Publisher


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', "last_name", "email")
    search_fields = ('first_name', "last_name")


class BookAdmin(admin.ModelAdmin):

    # 编辑列表
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date','title')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date', )

    # 编辑表单
    # fields = ( 'title', 'author', 'publisher')

    # 多对多 外键关系时可以设置
    filter_horizontal = ('author',)
    # filter_vertical = ('author',)

    # 一对多  ForeignKey
    raw_id_fields = ('publisher',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
