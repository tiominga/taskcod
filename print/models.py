from django.db import models
from task.models import Task
from django.core.exceptions import ValidationError
from datetime import date

class Print(models.Model):
    cod_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    date_add = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.image:
            raise ValidationError('Selecione uma imagem obrigatóriamente')

