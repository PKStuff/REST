from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.GETPOST, name='getpost'),
    path('<int:emp_id>/', views.GETPUTDELETE, name='GETPUTDELETE'),
]