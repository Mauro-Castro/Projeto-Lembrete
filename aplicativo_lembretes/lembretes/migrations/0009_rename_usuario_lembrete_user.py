# Generated by Django 5.0.7 on 2024-07-30 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lembretes', '0008_rename_user_lembrete_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lembrete',
            old_name='usuario',
            new_name='user',
        ),
    ]
