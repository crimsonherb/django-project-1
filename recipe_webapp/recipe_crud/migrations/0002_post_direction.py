# Generated by Django 4.1.1 on 2022-09-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='direction',
            field=models.TextField(null=True),
        ),
    ]
