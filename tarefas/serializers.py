from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['titulo', 'prazo', 'descricao', 'finalizada']
        extra_kwargs = {             
            'titulo': {'required': True}
        }
        
  
    def validate_prazo(self, prazo):
        if prazo < date(2000, 1, 1):
            raise serializers.ValidationError("O prazo não pode ser inferior ao ano 2000.")
        return prazo