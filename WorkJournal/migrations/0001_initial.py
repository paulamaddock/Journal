# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('edit_date', models.DateField()),
                ('entry_date', models.DateField()),
                ('entry_text', models.TextField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
