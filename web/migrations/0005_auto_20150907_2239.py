# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_judgement'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='judgement',
            unique_together=set([('judge', 'judged')]),
        ),
    ]
