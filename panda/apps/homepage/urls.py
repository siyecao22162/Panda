from django.conf.urls import url

from apps.homepage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage')
]
