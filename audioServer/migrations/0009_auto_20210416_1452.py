# Generated by Django 3.1.7 on 2021-04-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioServer', '0008_auto_20210415_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.CharField(max_length=50),
        ),
    ]
