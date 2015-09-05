# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150905_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='stereotype',
            field=models.IntegerField(choices=[(0, b'Jock'), (1, b'Hippie'), (2, b'Bro'), (3, b'Diva'), (4, b'Bookworm'), (5, b'Techie'), (6, b'Dancer'), (7, b'Emo')]),
        ),
    ]
