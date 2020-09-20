from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gig/<int:pk>', views.gig_detail_page, name='gig_detail'),
    path('create_gig', views.create_gig, name='create_gig'),
    path('my_gigs', views.my_gigs, name='my_gigs'),
    path('my_gigs/edit_gig/<int:pk>', views.edit_gig, name='edit_gig')
]
