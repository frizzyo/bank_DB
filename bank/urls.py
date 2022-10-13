from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('task1/', views.task_1, name='task_1'),
    path('task2/', views.task_2, name='task_2'),
    path('task3/', views.task_3, name='task_3'),
    path('client/new/', views.client_new, name='client_new'),
    path('creditinfo/new/', views.creditinfo_new, name='creditinfo_new'),
    path('credit/new/', views.credit_new, name='credit_new'),
]