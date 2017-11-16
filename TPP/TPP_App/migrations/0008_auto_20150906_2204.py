# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TPP_App', '0007_auto_20150328_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smallgroup',
            old_name='order',
            new_name='ordr',
        ),
    ]
