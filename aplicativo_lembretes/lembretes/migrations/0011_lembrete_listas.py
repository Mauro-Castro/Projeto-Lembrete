# Generated by Django 5.0.7 on 2024-07-31 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lembretes', '0010_lista'),
    ]

    operations = [
        migrations.AddField(
            model_name='lembrete',
            name='listas',
            field=models.ManyToManyField(blank=True, to='lembretes.lista'),
        ),
    ]
