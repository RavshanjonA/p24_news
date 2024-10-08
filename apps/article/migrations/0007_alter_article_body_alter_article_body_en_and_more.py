# Generated by Django 5.0.7 on 2024-08-13 16:19

import ckeditor_uploader.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_body_en_article_body_ru_article_body_uz_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artcicles', to='article.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Likes'),
        ),
        migrations.AlterField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, unique=True, verbose_name='SLG'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug_en',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='SLG'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug_ru',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='SLG'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug_uz',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='SLG'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[("('df', 'Draft')", 'Draft'), ('pb', 'Published')], default="('df', 'Draft')", max_length=15, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='article.tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_uz',
            field=models.CharField(max_length=256, null=True, verbose_name='Title'),
        ),
    ]
