# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from TPP_App.lib import TPPDataParser

from os import listdir

def populate_smallgroups_table( apps, schema_editor ):

    print '\nPopulating db table smallgroup with JSON test data ...'

    print '\nGetting smallgroup model from versioned app registry ...'
    SmallGroup = apps.get_model( 'TPP_App', 'SmallGroup' )
    db_alias = schema_editor.connection.alias

    print '\nGetting list of JSON data files names from app static/ subdirectory ...'
    static_dir_path = '/Users/srm/Documents/sandeep/cst/dev/TPP/TPP/TPP_App/static/'
    JSON_data_file_names = filter(
                             lambda file_name: \
                               file_name.__contains__( 'SmallGroupsData' ), \
                             listdir( static_dir_path )
                           )
    print JSON_data_file_names

    print '\nGetting parser to handle the JSON subgroup TPP data ...'
    parser = TPPDataParser()

    for file_name in JSON_data_file_names:
        file_path = static_dir_path + file_name
        print 'Opening file {}'.format( file_path )
        parser.load_small_groups( file_path, 'JSON' )
        sm_groups = parser.get_small_groups_aslist()

        print '\nCreating list of smallgroup model objects for bulk insertion ...'
        db_sm_groups = [
            SmallGroup(
                GAP_ID=str( sm_group.GAP_ID ).strip( '()' ),
                order=sm_group.order,
                GAP_desc=sm_group.GAP_desc,
                GAP_pickled_ID=sm_group.GAP_pickled_ID,
                index_LAN_subgroup=sm_group.index_LAN_subgroup,
                index_LCN_subgroup=sm_group.index_LCN_subgroup,
                index_LEAN_subgroup=sm_group.index_LEAN_subgroup,
                is_abelian=sm_group.is_abelian,
                comm_length=sm_group.comm_length,
                is_cyclic=sm_group.is_cyclic,
                is_elem_abelian=sm_group.is_elem_abelian,
                is_simple=sm_group.is_simple,
                comp_length=sm_group.comp_length,
                is_nilpotent=sm_group.is_nilpotent,
                nilpotency_class=sm_group.nilpotency_class,
                is_solvable=sm_group.is_solvable,
                derived_length=sm_group.derived_length,
                is_pgroup=sm_group.is_pgroup,
                generators=sm_group.generators,
                char_degrees=sm_group.char_degrees,
                D3=sm_group.D3,
                MBS_STPP_param_type=str( sm_group.MBS_STPP_param_type ).strip( '()' ),
                Beta0=sm_group.Beta0
            )
            for sm_group in sm_groups
        ]

        print '\nDoing the bulk insertion ...'
        SmallGroup.objects.using( db_alias ).bulk_create( db_sm_groups )

        print '\n{} SmallGroup objects successfully inserted and saved into smallgroups table'.\
              format( len( db_sm_groups ) )

    print 'Bulk insertion done ... a total of {} SmallGroup objects successfully inserted and saved into smallgroups table'.format( SmallGroup.objects.count() )


class Migration( migrations.Migration ):

    dependencies = [
        ( 'TPP_App', '0003_auto_20150224_2024' ),
    ]

    operations = [
        migrations.RunPython( populate_smallgroups_table ),
    ]
