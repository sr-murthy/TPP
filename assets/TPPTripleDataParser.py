'''
    Parser for the TPP triple raw data contained in static HTML tables containing subgroup TPP data and JSON files containing GAP small groups information.
'''
import collections, io, json

class TPPTripleDataParser:

    small_groups_JSON_schema = {
      'GAP_ID': { 'JSON_type': 'array', 'python_type': tuple, 'length': 2 },
      'order': { 'JSON_type': 'number', 'python_type': int },
      'GAP_desc': { 'JSON_type': 'string', 'python_type': str },
      'GAP_pickled_ID': { 'JSON_type': 'string', 'python_type': str },
      'index_LAN_subgroup': { 'JSON_type': 'number', 'python_type': int },
      'index_LCN_subgroup': { 'JSON_type': 'number', 'python_type': int },
      'index_LEAN_subgroup': { 'JSON_type': 'number', 'python_type': int },
      'is_abelian': { 'JSON_type': 'boolean', 'python_type': bool },
      'comm_length': { 'JSON_type': 'number', 'python_type': int },
      'is_cyclic': { 'JSON_type': 'boolean', 'python_type': bool },
      'is_elem_abelian': { 'JSON_type': 'boolean', 'python_type': bool },
      'is_simple': { 'JSON_type': 'boolean', 'python_type': bool },
      'comp_length': { 'JSON_type': 'number', 'python_type': int },
      'is_nilpotent': { 'JSON_type': 'boolean', 'python_type': bool },
      'nilpotency_class': { 'JSON_type': 'number', 'python_type': int },
      'is_solvable': { 'JSON_type': 'boolean', 'python_type': bool },
      'derived_length': { 'JSON_type': 'number', 'python_type': int },
      'is_pgroup': { 'JSON_type': 'boolean', 'python_type': bool },
      'generators': { 'JSON_type': 'string', 'python_type': str },
      'char_degrees': { 'JSON_type': 'string', 'python_type': str },
      'D3': { 'JSON_type': 'number', 'python_type': int },
      'MBS_STPP_param_type': { 'JSON_type': 'array', 'python_type': tuple, 'length': 3 },
      'Beta0': { 'JSON_type': 'number', 'python_type': int }
    }


    def __get_HTML_table_column_indices( self, row, count ):

        i = j = 0

        while count > 0:
            i = row.find( '<td>', i + 1 )
            if i != -1: count -= 1
            else: return ()

        return (i + 4, row.find( '</td>', i ))


    def __get_HTML_table_column_value( self, row, col_name ):

        col_val = ''
        col_indices = ()

        if col_name in [ 'GAP_ID', 'order' ]:
            col_indices += self.__get_HTML_table_column_indices( row, 1 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].translate( None, '[]* ' )
                col_val = tuple( int( s ) for s in col_val.split( ',' ) )
            else: return 'ERROR'
            if col_name == 'order': col_val = col_val[0]
        elif col_name == 'char_degrees':
            col_indices += self.__get_HTML_table_column_indices( row, 2 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].replace( ' ', '' )
            else: return 'ERROR'
        elif col_name == 'D3':
            col_indices += self.__get_HTML_table_column_indices( row, 3 )
            if col_indices != ():
                col_val = int( row[col_indices[0]:col_indices[1]].replace( ' ', '' ) )
        elif col_name in [ 'MBS_STPP_param_type', 'Beta0' ]:
            col_indices += self.__get_HTML_table_column_indices( row, 9 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].replace( ' ', '' )
                col_val = [int( s ) for s in col_val.split( ',' )]
                col_val.reverse()
                col_val = tuple( col_val )
                if col_name == 'Beta0':
                    col_val = col_val[0]*col_val[1]*col_val[2]
        else: return 'ERROR'

        return col_val


    def __get_HTML_table_row( self, HTML_data_file ):

        row_line = ''

        while True:
            line = HTML_data_file.readline().lower()
            if not line == '':
                if '<tr>' in line:
                    row_line += line.replace( ' ', '' )
                    while True:
                        line = HTML_data_file.readline().lower()
                        if not line == '':
                            row_line += line.strip().replace( ' ', '' )
                            if '</tr>' in line:
                                return row_line
                            else: continue
                        else: break
            else: return 'EOF'

        return row_line


    def get_small_groups_static_HTML_data( self, file_path ):

        HTML_data_file = open( file_path, 'r', 0 )
        SmallGroup = collections.namedtuple(
                  'SmallGroup', TPPTripleDataParser.small_groups_JSON_schema.keys()
                                      )
        row = ''
        i = 0
        print '\n'
        row = self.__get_HTML_table_row( HTML_data_file)

        while not row == 'EOF':
            ID = self.__get_HTML_table_column_value( row, 'GAP_ID' )
            ptype = self.__get_HTML_table_column_value( row, 'MBS_STPP_param_type' )
            group_rec = SmallGroup( GAP_ID=ID, order=ID[0], GAP_desc='',
            GAP_pickled_ID='', is_abelian=None, comm_length=None, is_cyclic=None,
            is_elem_abelian=None, is_simple=None, comp_length=None,
            is_nilpotent=None, nilpotency_class=None, is_solvable=None,
            derived_length=None, is_pgroup=None, generators=None,
            char_degrees=self.__get_HTML_table_column_value( row, 'char_degrees' ),
            D3=self.__get_HTML_table_column_value( row, 'D3' ),
            MBS_STPP_param_type=ptype, Beta0=ptype[0]*ptype[1]*ptype[2] )
            self.small_groups.update( {ID:group_rec} )
            i += 1
            row = self.__get_HTML_table_row( HTML_data_file )

        HTML_data_file.close()
        print 'Ordered dictionary of {} named tuples of small groups created.  File {} closed.'.format( len( self.small_groups ), HTML_data_file.name )


    def write_small_groups_JSON_file( self, file_dir, file_name, indent_num ):

        with io.open( file_dir + file_name, 'w', encoding='utf-8' ) as file:
            file.write( unicode( '[\n' ) )
            for count, small_group in enumerate( self.small_groups.values() ):
                if count:  file.write( unicode( ',\n' ) )
                JSON_obj = json.dumps( small_group._asdict(), \
                                       indent=indent_num, \
                                       ensure_ascii=False )
                file.write( unicode( JSON_obj ) )
            file.write( unicode( '\n]' ) )

        print '{} small group JSON objects successfully written to the file {}.'.\
              format( len( self.small_groups ), file.name )


    def read_small_groups_JSON_file( self, file_path, source ):

        sm_groups = collections.OrderedDict()
        decoder = json.JSONDecoder()

        with io.open( file_path, 'r', encoding='utf-8' ) as file:
            for line in file:
                if '{' in line and '}' in line:
                    sm_group = decoder.raw_decode( line )[0]
                    ID = tuple( sm_group['GAP_ID'] )
                    sm_group['GAP_ID'] = ID
                    if source in [ 'static HTML', 'JSON' ]:
                        sm_group['MBS_STPP_param_type'] = \
                          tuple( sm_group['MBS_STPP_param_type'] )
                        sm_group['index_LAN_subgroup'] = None
                        sm_group['index_LCN_subgroup'] = None
                        sm_group['index_LEAN_subgroup'] = None
                    elif source == 'GAP':
                        sm_group['order'] = ID[0]
                        sm_group['D3'] = None
                        sm_group['MBS_STPP_param_type'] = None
                        sm_group['Beta0'] = None
                    sm_group = collections.namedtuple( 'SmallGroup', \
                               TPPTripleDataParser.small_groups_JSON_schema.keys() )\
                               ( **sm_group )
                    sm_groups.update( {ID:sm_group} )

        print 'Ordered dictionary of {} named tuples of small groups loaded from JSON file {}.'.format( len( sm_groups ), file.name )
        return sm_groups


    def update_small_groups( self, groups_updated_info ):

        count = 0

        for ID in self.small_groups.keys():
            if ID in groups_updated_info.keys():
                small_group = self.small_groups[ID]._asdict()
                update_group = groups_updated_info[ID]._asdict()
                for key in update_group.keys():
                    if not key in [ 'GAP_ID', 'Beta0', 'MBS_STPP_param_type' ]:
                        small_group[key] = update_group[key]
                small_group = collections.namedtuple( 'SmallGroup', \
                           TPPTripleDataParser.small_groups_JSON_schema.keys() )\
                           ( **small_group )
                self.small_groups[ID] = small_group
                count += 1

        print 'Updated {} small groups in parser.'.format( count )


    def get_small_groups( self, asdict ):

        if asdict: return self.small_groups._asdict()
        else: return self.small_groups


    def __init__( self ):

        print 'Creating a new TPPTripleDataParser instance ...'
        self.small_groups = collections.OrderedDict()
