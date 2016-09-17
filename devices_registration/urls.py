from django.conf.urls import url

from . import views


# Browser: IP:8000/reg/URL_ADDRESS 

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
