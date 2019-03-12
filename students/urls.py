from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('new/', views.new),
    path('<int:pk>/detail/', views.detail),
    path('<int:pk>/delete/', views.delete),

]