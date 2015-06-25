# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwshortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=500),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(verbose_name='URL', max_length=500),
        ),
    ]
