# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TPP_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smallgroup',
            name='index_LAN_subgroup',
            field=models.IntegerField(null=True, verbose_name=b'Index of a largest abelian normal subgroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='smallgroup',
            name='index_LCN_subgroup',
            field=models.IntegerField(null=True, verbose_name=b'Index of a largest cyclic normal subgroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='smallgroup',
            name='index_LEAN_subgroup',
            field=models.IntegerField(null=True, verbose_name=b'Index of a largest elementary abelian normal subgroup'),
            preserve_default=True,
        ),
    ]
