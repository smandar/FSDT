from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^modify/', views.modify, name='modify'),
    url(r'^create_contact/', views.create_contact, name='create_contact'),
    url(r'^update_contact/', views.update_contact, name='update_contact'),
]
