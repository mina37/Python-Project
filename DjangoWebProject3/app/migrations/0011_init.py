# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_init'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='location',
            field=models.FileField(upload_to='/Users/Mina37/documents/visual studio 2015/Projects/DjangoWebProject3/DjangoWebProject3/document'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='file name'),
        ),
    ]
