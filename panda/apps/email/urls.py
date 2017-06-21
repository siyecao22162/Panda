from django.conf.urls import url

from apps.email import views

urlpatterns = [
    url(r'^$', views.BroadcastView.as_view(), name='broadcast')
]
