from django.contrib import admin
from .models import Publisher,Author,Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin): #修改列表
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')  #添加搜索框

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_provice','country','website')
    search_fields = ('name',)
    list_filter = ('name',)
    fields = ('name','country','city','address','state_provice','website')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',) #添加日期过滤器  #添加一个元组,逗号不可省略
    date_hierarchy = 'publication_date'  #日期过滤器 添加字符串,显示在顶部
    search_fields = ('title',)
    ordering = ('-publication_date',)  #定义排序,注意是个元组,一个元素时逗号不要省略
    #fields = ('title','publisher','authors')  #自定义字段显示顺序  #隐藏publication_date字段
    filter_horizontal = ('authors',)  #添加JavaScript 过滤器界面，可以动态搜索选项
    #filter_vertical = ('authors',) #作用与filter_horizontal类似
    raw_id_fields = ('publisher',)  #一个外键字段名称元组，各个字段在管理后台中显示为简单的文本输入框


admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)