# Generated by Django 4.2.15 on 2024-08-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='ChatGpt Всех Убьёт')),
                ('announcement', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='ChatGpt написал этот сайт')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
