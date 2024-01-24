# Generated by Django 5.0 on 2024-01-13 16:41

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('tipo_de_vaga', models.CharField(choices=[('CLT', 'clt'), ('PJ', 'pj'), ('FREELANCER', 'freelancer')], default='', max_length=100)),
                ('descricao', models.TextField()),
                ('local', models.CharField(max_length=200)),
                ('salario', models.CharField(max_length=20)),
                ('publicada', models.BooleanField(default=False)),
                ('data_publicada', models.DateTimeField(default=datetime.datetime.now)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
