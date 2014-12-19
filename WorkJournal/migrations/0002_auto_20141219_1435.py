# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkJournal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='edit_date',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
    ]
