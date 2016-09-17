from django.conf.urls import url

from . import views


# Browser: IP:8000/dashboard/URL_ADDRESS 

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^dev_request', views.dev_request, name='dev_request'),
    url(r'^dev_check', views.dev_check, name='dev_check'),
    url(r'^dev_rejected', views.dev_rejected, name='dev_rejected'),
    url(r'^dev_edit', views.dev_edit, name='dev_edit'),
    url(r'^device_save_reject_del', views.device_save_reject_del, name='device_save_reject_del'),

]
