# Generated by Django 5.0.7 on 2024-08-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
