# Generated by Django 5.0 on 2024-01-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='tipo_de_vaga',
            field=models.CharField(choices=[('CLT', 'clt'), ('PJ', 'pj'), ('HOME OFFICE', 'home office'), ('MENOR APRENDIZ', 'menor aprendiz'), ('FREELANCER', 'freelancer'), ('DIARISTAS', 'diaristas')], default='', max_length=100),
        ),
    ]
