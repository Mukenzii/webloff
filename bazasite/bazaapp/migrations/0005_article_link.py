# Generated by Django 5.0.3 on 2024-03-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaapp', '0004_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]