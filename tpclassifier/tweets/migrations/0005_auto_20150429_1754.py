# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20150429_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='text',
        ),
        migrations.AddField(
            model_name='tweet',
            name='raw_text',
            field=models.CharField(help_text=b"The tweet's raw text", max_length=255, null=True, blank=True),
        ),
    ]
