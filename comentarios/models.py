from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Atualizado em')

    class Meta:
        abstract = True


class Comentario(Base):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-Mail')
    comentario = models.TextField(verbose_name='Comentario')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuario', blank=True, null=True)
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.nome_comentario
