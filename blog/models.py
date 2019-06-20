from django.db import models

# Create your models here.

class Articel(models.Model):

    #关于创建字段的方法可以去django的官方网站去查看
    #https://docs.djangoproject.com/en/2.2/ref/models/fields/
    #可以翻译成中文就可以查看了


    #相当于我们创建了一个title字段，并且是一个char类型的，这个CharField方法必须传入一个最大长度选项max_length，这里我们设置为最大64个字符,h
    #CharField方法还有第二个参数是一个可选参数，默认值default，
    title=models.CharField(max_length=64,default='title');


    #创建一个Text字段默认为null
    content=models.TextField(null=True);


    #创建一个发布日期,添加条目的时候直接自动添加时间
    pub_time=models.DateTimeField(auto_now=True)


    #   django 3.0以后使用现在使用的 之前则使用现在注释掉的
    # def __unicode__(self):
    #     return self.title

    def __str__(self):
        return self.title

