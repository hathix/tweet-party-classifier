# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20150423_0428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='raw_text',
            new_name='text',
        ),
    ]
