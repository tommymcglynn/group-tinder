# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female')])),
                ('stereotype', models.CharField(max_length=1, choices=[(0, b'Jock'), (1, b'Hippie'), (2, b'Bro'), (3, b'Diva'), (4, b'Bookworm'), (5, b'Techie'), (6, b'Dancer'), (7, b'Emo')])),
            ],
        ),
    ]
