# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration( migrations.Migration ):

    dependencies = [
        ( 'TPP_App', '0004_auto_20150302_0953' ),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallgroup',
            name='Beta0',
            field=models.IntegerField( verbose_name=b'Subgroup TPP capacity (B0)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='D3',
            field=models.IntegerField( verbose_name=b'Sum of cubes of character degrees (D3)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='MBS_STPP_param_type',
            field=models.CommaSeparatedIntegerField( max_length=16, verbose_name=b'Maximum-by-size (MBS) subgroup TPP (STPP) triple type' ),
            preserve_default=True,
        ),
    ]
