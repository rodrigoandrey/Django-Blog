from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Atualizado em')
    status = models.BooleanField('Status', default=True)

    class Meta:
        abstract = True


class Categoria(Base):
    nome_categoria = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.nome_categoria
