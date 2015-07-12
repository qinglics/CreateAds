# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ad_id', models.CharField(max_length=100)),
                ('ad_title', models.TextField()),
                ('ad_text', models.TextField()),
                ('ad_pics', models.TextField()),
                ('others', models.TextField()),
            ],
        ),
    ]
