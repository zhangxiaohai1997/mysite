from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return  HttpResponse('Hello, books.')

# def search_form(request):
#     return render(request,'search_form.html')

#def search(request):
    # if 'q' in request.GET and request.GET['q']:   #检查 request.GET 中有没有 'q' ,request.GET['q'] 是不是空值，
    #   q=request.GET['q']
    #   books=Book.objects.filter(title__icontains=q)    #在图书表中查找所有书名中包含查询词条的书
    #   return render(request,'search_results.html',{'books':books,'query':q})  #字典中的值替换模板变量
    # else:
    #     return render(request,'search_form.html',{'error':True})

    # errors=[]   #空列表也表示为false
    # if 'q' in request.GET:  #任何输入的字符都能接受,包括空值
    #     q=request.GET['q']
    #     if not q:
    #         errors.append('Enter a search term.')
    #     elif len(q)>20:  #验证输入的字符串是否超过20个,若超过需重新输入
    #         errors.append('Please enter at most 20 characters.')
    #     else:
    #         books=Book.objects.filter(title__icontains=q)
    #         return render(request,'search_results.html',{'books':books,'query':q})
    #     return render(request,'search_form.html',{'errors':errors})

def search(request):
    errors=[]
    if 'q' in request.GET:  #包括空值
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',{'books': books, 'query': q})
    return render(request,"search_form.html",{'errors':errors})

def contact(request):
    if request.method=='POST':  #判断请求方法是否为post
        form=ContactForm(request.POST)  #将想要发送的请求传到变量form中
        if form.is_valid():
            cd=form.cleaned_data   #清理数据,返回字符串对象
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','zhangzihao@163.com'),['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form=ContactForm(initial={'subject':'I love your site!','message':'It is very beautiful'})  #如果不是post请求,就创建一个空表单,initial参数设置初始值
    return  render(request,'contact_form.html',{'form':form})


#HttpRequest 对象的方法和属性
# def current_url_view_good(request):
#     return HttpResponse("Welcome to the page at %s" % request.get_host())

#request.META 的值是一个 Python 字典，包含请求的所有 HTTP 首部，例如用户的 IP 地址和用户代理（user agent，通常是 Web 浏览器的名称和版本）。
def ua_display_good1(request):
    try:
        ua = request.META['REMOTE_ADDR']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)