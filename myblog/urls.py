from django.urls import path
from myblog import views

urlpatterns = [
    path('',views.bloghome),
]