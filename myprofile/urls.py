from django.conf.urls import url
from myprofile import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]