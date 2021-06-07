from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=200) # Charfield é para indicar o tipo, no caso vai ser de letras
    descricao = models.TextField(blank=True, null=True) # TextField não tem limite de caractere
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação') # O auto_now serve para que toda vez que um usuário criar um registro, o sistema automaticamente anotar qual foi a data e hora de criação
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Ou seja estou dizendo que se o User for deletado, ele exclua todos os eventos dele


    class Meta:
        db_table = 'Evento'

    def __str__(self):
        return self.titulo # Toda vez que alguem chamar esse objeto, mesmo que não acessa-lo ele irá aparecer o titulo ao inves de object(1)
