from django.conf.urls import url, include

from apps.homepage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^promotion/$', views.PromotionPageView.as_view(), name='promotion'),
    url(r'^checkout/paypal', include('paypal.express.urls')),
]