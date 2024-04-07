from django.urls import path
from . import views

urlpatterns = [
    path('add-to-list/', views.add_to_list, name='add-to-list'),
    path('', views.index, name='index'),
]