import uuid
from datetime import date
from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from stdimage.models import StdImageField
from django.utils import timezone


# Rename function for posts images.
def get_file_path(_instace, filename) -> str:
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    file_path = f'post_img/{year}/{month}/{day}/'
    ext = filename.split('.')[-1]
    file_name = f'{file_path}{uuid.uuid4()}.{ext}'
    return file_name


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Atualizado em')

    class Meta:
        abstract = True


class Post(Base):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True,
                                       verbose_name='Categoria')
    imagem_post = StdImageField(upload_to=get_file_path, blank=True, verbose_name='Imagem',
                                variations={'thumb': {'width': 300, 'height': 200, 'crop': True}})
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.titulo_post
