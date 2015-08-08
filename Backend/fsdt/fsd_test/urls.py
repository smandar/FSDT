from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^modify/', views.modify, name='modify'),
]
