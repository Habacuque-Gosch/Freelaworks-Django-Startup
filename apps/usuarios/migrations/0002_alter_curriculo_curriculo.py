# Generated by Django 5.0 on 2024-01-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='curriculo',
            field=models.FileField(blank=True, default=2, upload_to='curriculo/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]