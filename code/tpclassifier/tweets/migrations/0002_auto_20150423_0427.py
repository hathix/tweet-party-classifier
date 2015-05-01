# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='raw_text',
            field=models.CharField(default='', help_text=b"The tweet's raw text", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='party',
            field=models.IntegerField(default=0, help_text=b"Party of tweet's author", choices=[(0, b'Democrat'), (1, b'Republican')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.IntegerField(default=0, help_text=b'Arbitrarily assigned ID to easily identify tweets'),
            preserve_default=False,
        ),
    ]
