from django.core.exceptions import ValidationError
from tarefas.models import Task
from django.db.models import Q
from django.test import TestCase

class TitleTest(TestCase):

    
    def test_title_not_blank(self):
        Task.objects.get(
            Q(titulo__startswith='')
        )
        with self.assertRaises(ValidationError):
            self.tasks.full_clean()