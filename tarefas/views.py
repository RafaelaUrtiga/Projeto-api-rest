from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from.models import Task
from .serializers import TaskSerializer
from django.http import Http404, HttpResponse
import json
from django.contrib.auth.models import User

class TaskList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail (APIView):

    def get_object(self, id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            raise Http404
    
    def get(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        task = self.get_object(id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ExportTasks(APIView):
 
    def get(self, request):
        tasks = Task.objects.all()
        format = request.GET.get('format')
        
        if format == 'json':
            return self.export_to_json(tasks)
        elif format == 'txt':
            return self.export_to_txt(tasks)
        else:
            return Response({'error': 'Invalid format. Please specify "json" or "txt".'}, status=400)
    
        
    def export_to_json(self, tasks):
        serializer = TaskSerializer(tasks, many=True)
        json_data = json.dumps(serializer.data, indent=4)  # converte o serializer em string
        response = HttpResponse(json_data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="tasks.json"'
        return response
    
    def export_to_txt(self, tasks):
        content = ''
        for task in tasks:
            serializer_task = TaskSerializer(task).data
            content += (
                f'Titulo: {serializer_task["titulo"]}, '
                f'Descricao: {serializer_task["descricao"]}, '
                f'Prazo: {serializer_task["prazo"]}, '
                f'Finalizada: {serializer_task["finalizada"]}\n'
            )
        
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="tasks.txt"'
        return response