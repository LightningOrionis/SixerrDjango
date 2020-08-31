from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gig/<int:pk>', views.gig_detail_page, name='gig_detail')
]
