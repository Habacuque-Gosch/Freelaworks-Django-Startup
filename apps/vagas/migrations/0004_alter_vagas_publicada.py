# Generated by Django 5.0 on 2024-01-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0003_alter_vagas_tipo_de_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]