from django.conf.urls import url

from big_geo_ballarat import views

app_name = 'big_geo_ballarat'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
