# Generated by Django 4.1.1 on 2022-09-12 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
