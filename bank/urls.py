from django.urls import path

from . import views

urlpatterns = [
    path('task1/', views.task_1, name='task_1'),
    path('task2/', views.task_2, name='task_2'),
    path('task3/', views.task_3, name='task_3'),
]