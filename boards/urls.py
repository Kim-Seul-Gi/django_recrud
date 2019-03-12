from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'), # /boards/ = board:index
    path('new/', views.new, name='new'), # /boards/new/
    # path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    # path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
