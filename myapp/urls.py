from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('members',views.member),
    path('contact',views.contact),
]