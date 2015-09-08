# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20150907_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agreed', models.ForeignKey(related_name='web_match_agreed', verbose_name=b'Matched in agreement', to='web.Person')),
                ('initiated', models.ForeignKey(related_name='web_match_initiated', verbose_name=b'Initiator of match', to='web.Person')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('initiated', 'agreed')]),
        ),
    ]
