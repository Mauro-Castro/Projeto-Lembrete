# Generated by Django 5.0.7 on 2024-07-26 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prioridades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lembrete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_lembrete', models.DateTimeField()),
                ('prioridade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lembretes', to='prioridades.prioridade')),
            ],
        ),
    ]