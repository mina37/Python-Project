# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_init'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='location',
            field=models.FileField(upload_to=''),
        ),
    ]
