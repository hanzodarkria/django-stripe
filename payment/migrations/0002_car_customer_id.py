# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='customer_id',
            field=models.CharField(default='', max_length=234),
            preserve_default=False,
        ),
    ]
