# Generated by Django 5.0.3 on 2024-03-22 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaapp', '0005_article_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bazaapp.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
