# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mig'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(verbose_name='First Name', max_length=50)),
                ('lname', models.CharField(verbose_name='Last Name', max_length=50)),
                ('uname', models.CharField(verbose_name='User Name', max_length=50)),
                ('passwords', models.CharField(verbose_name='Password', max_length=50)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
            ],
        ),
    ]
