# Generated by Django 5.0.3 on 2024-03-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaapp', '0002_category_delete_article_delete_articlecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
