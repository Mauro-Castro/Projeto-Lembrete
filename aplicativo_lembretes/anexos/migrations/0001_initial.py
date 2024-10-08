# Generated by Django 5.0.7 on 2024-07-26 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lembretes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='anexos/')),
                ('descricao', models.TextField()),
                ('lembrete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lembretes.lembrete')),
            ],
        ),
    ]
