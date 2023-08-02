from django.urls import path
from myblog import views

urlpatterns = [
    path('',views.bloghome),
    path('<str:slug>',views.blogpost)
]