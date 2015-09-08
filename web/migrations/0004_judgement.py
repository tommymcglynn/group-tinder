# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150905_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judgement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruling', models.BooleanField(verbose_name=b'the value of the judgement')),
                ('judge', models.ForeignKey(related_name='web_judgement_made', verbose_name=b'the person judging', to='web.Person')),
                ('judged', models.ForeignKey(related_name='web_judgement_received', verbose_name=b'the person being judged', to='web.Person')),
            ],
        ),
    ]
