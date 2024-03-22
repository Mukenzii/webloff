# Generated by Django 5.0.3 on 2024-03-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaapp', '0003_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Kontent', 'verbose_name_plural': 'Kontentlar'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
