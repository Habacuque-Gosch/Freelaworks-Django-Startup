# Generated by Django 5.0 on 2024-01-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0002_delete_cadastroforms_delete_loginforms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=150)),
                ('numero_funcionarios', models.CharField(max_length=100)),
                ('numero_telefone', models.CharField(max_length=100)),
            ],
        ),
    ]
