# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_init'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='vote',
        ),
    ]
