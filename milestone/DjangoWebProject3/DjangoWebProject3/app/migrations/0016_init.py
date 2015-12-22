# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_init'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date',
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True),
        ),
    ]
