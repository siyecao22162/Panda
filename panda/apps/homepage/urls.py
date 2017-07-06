from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^promotion/$', views.PromotionPageView.as_view(), name='promotion'),
    url(r'^msg_sent$', views.msg_sent, name='message_sent')
]
