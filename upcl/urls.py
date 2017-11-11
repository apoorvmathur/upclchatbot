from django.conf.urls import url
from upcl import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'getBillAmount/$', views.getBillAmount, name='Get Bill'),
]
