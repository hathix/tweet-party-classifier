# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20150423_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='name',
            field=models.CharField(help_text=b"The person's name, including whether they are a Represenative or Senator", max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='party',
            field=models.IntegerField(blank=True, help_text=b"Party of tweet's author", null=True, choices=[(0, b'Democrat'), (1, b'Republican')]),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='raw_text',
            field=models.CharField(help_text=b"The tweet's raw text", max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.IntegerField(help_text=b'Arbitrarily assigned ID to easily identify tweets', null=True, blank=True),
        ),
    ]
