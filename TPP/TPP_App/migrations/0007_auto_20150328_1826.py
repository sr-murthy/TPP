# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def sort_small_group_MBS_STPP_param_type( apps, schema_editor ):

    print 'Changing the sort order of the MBS_STPP_param_type field of SmallGroup model objects, e.g. (1,2,3) will become (3,2,1)'
    SmallGroup = apps.get_model( 'TPP_App', 'SmallGroup' )
    db_alias = schema_editor.connection.alias

    sm_groups_iter = SmallGroup.objects.using( db_alias ).all().iterator()
    updated = 0
    for sm_group in sm_groups_iter:
        param_type = sm_group.MBS_STPP_param_type
        if not param_type == 'None':
            param_type = [int( token.strip( ' ' ) ) \
                          for token in param_type.split( ',' )]
            if not param_type[0] >= param_type[1] >= param_type[2]:
                param_type.reverse()
                sm_group.MBS_STPP_param_type = unicode( str( param_type ).strip( '[]' ) )
                sm_group.save()
                updated += 1
        else:
            sm_group.MBS_STPP_param_type = '{},{},{}'.format( sm_group.order, 1, 1 )
            sm_group.save()
            updated += 1

    print 'MBS_STPP_param_type field updated in {} SmallGroup objects'.format( updated )


class Migration( migrations.Migration ):

    dependencies = [
        ( 'TPP_App', '0006_auto_20150328_1740' ),
    ]

    operations = [
        migrations.RunPython( sort_small_group_MBS_STPP_param_type ),
    ]
