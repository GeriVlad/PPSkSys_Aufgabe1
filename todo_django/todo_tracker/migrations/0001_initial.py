# Generated by Django 3.0.6 on 2020-05-24 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=160)),
                ('deadline', models.DateField(default=datetime.date.today, null=True)),
                ('progress', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
