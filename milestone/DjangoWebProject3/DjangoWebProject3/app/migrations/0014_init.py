# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_init'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date',
        ),
    ]
