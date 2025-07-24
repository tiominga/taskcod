from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Task(models.Model):
    cod_user = models.IntegerField()
    id_clinica = models.IntegerField()
    tipo = models.CharField(max_length=25)
    prioridade = models.IntegerField()
    caminho = models.CharField(max_length=200)
    descricao = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)


    def clean(self):
        if not self.id_clinica:
            raise ValidationError('O id da clínica é obrigatório. Coloque 1 caso a requisição seja de sua autoria.')
        if not self.tipo:
            raise ValidationError('Escolha o tipo')
        if not self.prioridade:
            raise ValidationError('Escolha a prioridade')
        if not self.caminho:
            raise ValidationError('Informe o caminho que o programador deve seguir para encontrar o erro')
        if not self.descricao:
            raise ValidationError('A descrição é obrigatórios')
        if len(self.descricao) < 15:
            raise ValidationError('A descrição precisa de ao menos 15 letras')    


