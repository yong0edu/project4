from django.urls import path

from pagination import views

urlpatterns = [
    path('insert', views.insert, name='insert'),

]
