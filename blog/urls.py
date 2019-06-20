from django.urls import path,re_path
from . import views
#关于path的配置可以在官网文档中查看【https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path】

app_name='blog';
urlpatterns = [
    path('', views.index),
    path('list/', views.list),
    path('data/', views.getdata),
    path('show/<int:id>/',views.pageshow,name='show'),
    path('edit/<int:id>',views.editpage,name='editpage'),
    path('addcontent/',views.addcontent,name='addcontent'),
    path('updata/<int:id>/',views.updatapage,name='updata'),
    path('dataleast',views.updata,name='dataleast')
]