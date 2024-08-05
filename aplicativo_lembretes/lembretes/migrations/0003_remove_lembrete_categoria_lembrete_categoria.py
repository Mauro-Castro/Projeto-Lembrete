# Generated by Django 5.0.7 on 2024-07-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0003_lembrete'),
        ('lembretes', '0002_lembrete_categoria_alter_lembrete_prioridade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lembrete',
            name='categoria',
        ),
        migrations.AddField(
            model_name='lembrete',
            name='categoria',
            field=models.ManyToManyField(related_name='lembretes_app1', to='categorias.categoria'),
        ),
    ]
