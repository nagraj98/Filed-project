# Generated by Django 3.1.7 on 2021-04-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioServer', '0007_auto_20210415_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='dateupload',
        ),
        migrations.AlterField(
            model_name='podcast',
            name='timeupload',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
