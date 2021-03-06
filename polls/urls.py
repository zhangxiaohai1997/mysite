from django.conf.urls import url
from .import views

#app_name="polls"
urlpatterns=[
    url('^$',views.index,name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #用于添加新问题的网页
 #   url(r'^new_question/$',views.new_question,name='new_question'),
]
