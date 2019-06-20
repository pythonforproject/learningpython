from django.shortcuts import render
from . import models

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

#列表
def index(res):
    #获取所有数据条目
    alllist=models.Articel.objects.all();
    print(alllist)
    return render(res,'blog/index.html',{'alllist':alllist});

#页面详情
def pageshow(res,id=None):
    if id is None:
        print('aaa');
    pageshows=models.Articel.objects.get(id=id);
    return render(res,'blog/pageshow.html',{'pageshows':pageshows});

#新增页面
def editpage(res,id):
    if str(id)=='0':
        return render(res,'blog/edit_page.html')
    shows=models.Articel.objects.get(id=id)
    return render(res,'blog/edit_page.html',{'show':shows})


#新增提交地址
def addcontent(res):
    id=res.POST.get('id','0')
    title=res.POST.get('title')
    content=res.POST.get('content')
    if id=='0':
        models.Articel.objects.create(title=title,content=content);
        #调用index方法因为添加成功我们要跳转到index页面
        return index(res)
    rows=models.Articel.objects.get(id=id)
    rows.title=title
    rows.content=content
    #执行更新
    rows.save()
    # 跳转至文章页面
    return HttpResponseRedirect('/blog/')
    # return pageshow(res,id=rows.id);
# render(res,'blog/pageshow.html',{'pageshows':rows})

#修改文章
def updatapage(res,id=None):
    shows=models.Articel.objects.get(id=id);
    return render(res,'blog/updata.html',{'show':shows})

#提交更新数据
def updata(res):
    id=res.POST.get('id');
    title=res.POST.get('title');
    content=res.POST.get('content');
    models.Articel.objects.update(title=title,id=id,content=content);
    return pageshow(res,id)


def list(res):
    print('dsadsad','dsadsadas','22232dw');
    classlist=['dsadsa','232222'];
    arrlength=len(classlist);
    print(classlist[0]);
    renderData={
        'hello':'hello blog',
        'test':'test python',
        'title':'我的第一个python程序'
    }
    age=20
    if age>10:
        print('your age is', age)
    x=20;
    if x:
        print('true')
    else:
        print('false')
    names = ['Michael', 'Bob', 'Tracy'];
    s=[i.lower() for i in names]
    print(s);

    for name in names:
        print(name)
    #return HttpResponse('list');
    return render(res, 'blog/index.html', renderData)

#测试从数据库读取数据
def getdata(res):
    articel=models.Articel.objects.get(pk=1);
    return render(res,'blog/data.html',{'articel':articel})