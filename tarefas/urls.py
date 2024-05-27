from django.urls import path
from .views import TaskList, TaskDetail, ExportTasks
urlpatterns = [
    path('tarefas/', TaskList.as_view(), name='task-list'),
    path('tarefas/<int:id>/', TaskDetail.as_view(), name='task-detail'),
    path('export/', ExportTasks.as_view(), name='task-export'),
]
