# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TPP_App', '0002_auto_20150221_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallgroup',
            name='is_abelian',
            field=models.BooleanField(default=None, verbose_name=b'Abelian group?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='is_cyclic',
            field=models.BooleanField(default=None, verbose_name=b'Cyclic group?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='is_elem_abelian',
            field=models.BooleanField(default=None, verbose_name=b'Elementary abelian group?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='is_nilpotent',
            field=models.BooleanField(default=None, verbose_name=b'Nilpotent group?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='is_pgroup',
            field=models.BooleanField(default=None, verbose_name=b'Is p-group?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='is_simple',
            field=models.BooleanField(default=None, verbose_name=b'Simple group?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='is_solvable',
            field=models.BooleanField(default=None, verbose_name=b'Solvable group?'),
            preserve_default=True,
        ),
    ]
