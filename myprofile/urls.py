from django.conf.urls import url
from myprofile import views

app_name = 'myprofile'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]