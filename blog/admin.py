from django.contrib import admin
# Register your models here.
from .models import Articel

#配置类
class ArticelAdmin(admin.ModelAdmin):
    #让新闻列表按照我们指定的字段进行显示,这里的字段名必须是字符串
    list_display = ('id','title','content','pub_time')

    #增加过滤器,这样列表的右侧就会多出一个时间过滤模块
    #注意：因为我们这里使用的是tuple类型，只有一个值的情况下  必须在结尾处加一个逗号
    list_filter = ('pub_time',)



admin.site.register(Articel,ArticelAdmin)