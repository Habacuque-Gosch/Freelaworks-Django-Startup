# Generated by Django 5.0 on 2024-01-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0004_alter_vagas_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='numero_telefone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
