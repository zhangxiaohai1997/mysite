from django.conf.urls import url
from  .import views


urlpatterns=[
    url(r'^$',views.index,name='index'),
    #url(r'^search_form/$',views.search_form,name="search_form"),
    url(r'^search/$',views.search,name="search"),
    url(r'^contact/$',views.contact,name="contact"),

    #url(r'^current/$',views.current_url_view_good,name="current")
    url(r'^ua/$',views.ua_display_good1,name="ua")
]