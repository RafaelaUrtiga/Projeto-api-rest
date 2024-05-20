from django.urls import path
from .views import TaskList, TaskDetail, ExportToTXT, ExportToJSON
urlpatterns = [
    path('tarefas/', TaskList.as_view(), name='task-list'),
    path('tarefas/<int:id>/', TaskDetail.as_view(), name='task-detail'),
    path('export/json/', ExportToJSON.as_view(), name='task-export-json'),
    path('export/txt/', ExportToTXT.as_view(), name='task-export-txt'),
]
