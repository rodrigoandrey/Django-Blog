# Generated by Django 3.1.7 on 2021-03-12 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated At')),
                ('titulo_post', models.CharField(max_length=255, verbose_name='Título')),
                ('conteudo_post', models.TextField(verbose_name='Conteúdo')),
                ('excerto_post', models.TextField(verbose_name='Excerto')),
                ('imagem_post', models.ImageField(blank=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem')),
                ('publicado_post', models.BooleanField(default=False, verbose_name='Publicado')),
                ('autor_post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categoria_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria', verbose_name='Categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
