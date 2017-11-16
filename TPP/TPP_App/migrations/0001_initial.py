# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmallGroup',
            fields=[
                ('GAP_ID', models.CommaSeparatedIntegerField(max_length=14, serialize=False, verbose_name=b'GAP small group ID', primary_key=True)),
                ('order', models.IntegerField(verbose_name=b'Group order')),
                ('GAP_desc', models.CharField(max_length=100, verbose_name=b'GAP structure description')),
                ('GAP_pickled_ID', models.CharField(max_length=250, null=True, verbose_name=b'GAP IO pickled string representation')),
                ('is_abelian', models.BooleanField(verbose_name=b'Abelian group?')),
                ('comm_length', models.IntegerField(verbose_name=b'Commutator length')),
                ('is_cyclic', models.BooleanField(verbose_name=b'Cyclic group?')),
                ('is_elem_abelian', models.BooleanField(verbose_name=b'Elementary abelian group?')),
                ('is_simple', models.BooleanField(verbose_name=b'Simple group?')),
                ('comp_length', models.IntegerField(verbose_name=b'Composition length')),
                ('is_nilpotent', models.BooleanField(verbose_name=b'Nilpotent group?')),
                ('nilpotency_class', models.IntegerField(null=True, verbose_name=b'Nilpotency class')),
                ('is_solvable', models.BooleanField(verbose_name=b'Solvable group?')),
                ('derived_length', models.IntegerField(null=True, verbose_name=b'Derived length')),
                ('is_pgroup', models.BooleanField(verbose_name=b'Is p-group?')),
                ('generators', models.CharField(max_length=250, verbose_name=b'Generators and orders')),
                ('char_degrees', models.CharField(max_length=250, verbose_name=b'Character degrees and multiplicities')),
                ('D3', models.IntegerField(verbose_name=b'Sum of cubes of character degrees')),
                ('MBS_STPP_param_type', models.CommaSeparatedIntegerField(max_length=16, verbose_name=b'Maximum-by-size subgroup TPP triple parameter type')),
                ('Beta0', models.IntegerField(verbose_name=b'Subgroup TPP capacity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
