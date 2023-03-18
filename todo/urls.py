from django.urls import path

from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='TaskList'),
    path('<int:pk>', TaskDetail.as_view(), name='TaskDetail'),
    path('create/', TaskCreate.as_view(), name='TaskCreate'),
]
