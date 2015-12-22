# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_init'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='uname',
            field=models.CharField(max_length=255, default=True),
            preserve_default=False,
        ),
    ]
