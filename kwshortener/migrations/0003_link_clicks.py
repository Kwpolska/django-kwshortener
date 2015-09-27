# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwshortener', '0002_auto_20150625_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='clicks',
            field=models.IntegerField(default=0, verbose_name='Clicks'),
        ),
    ]
