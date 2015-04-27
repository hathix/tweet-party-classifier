# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_id', models.IntegerField(help_text=b'Arbitrarily assigned ID to easily identify tweets', null=True, blank=True)),
                ('party', models.IntegerField(blank=True, help_text=b"Party of tweet's author", null=True, choices=[(0, b'Democrat'), (1, b'Republican')])),
                ('name', models.CharField(help_text=b"The person's name, including whether they are a Represenative or Senator", max_length=255)),
            ],
        ),
    ]
