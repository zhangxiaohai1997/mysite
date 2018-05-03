from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
#from .forms import QuestionForm

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request,'polls/detail.html',{'question':question})
def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)  #如果异常返回404错误
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        #发生choice未找到异常时,重新返回表单页面,并给出提示信息
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #成功处理数据后,自动跳转到结果页面,防止用户连续多次提交
        return  HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

# def new_question(request):
#     """用于添加新问题"""
#     if request.method!='POST':
#         form=QuestionForm()
#     else:
#         form=QuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("polls:new_question"))
#
#     context={'form':form}
#     return render(request,'polls/new_question.html',context)
