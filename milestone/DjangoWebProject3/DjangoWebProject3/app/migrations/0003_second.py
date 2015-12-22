# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_init001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='location',
            field=models.FileField(upload_to=''),
        ),
    ]
