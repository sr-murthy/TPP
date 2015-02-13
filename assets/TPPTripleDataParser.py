'''
    Parser for the TPP triple raw data contained in static HTML tables located offline,
    and online at http://www2.informatik.uni-halle.de/da/hedtke/tpp/
'''
import collections, io, json

class TPPTripleDataParser:

    small_groups_JSON_schema = {
      'desc': { 'type': 'string', 'python_type': str },
      'order': { 'type': 'number', 'python_type': int },
      'GAP_ID': { 'type': 'array', 'python_type': tuple, 'length': 2 },
      'GAP_desc': { 'type': 'string', 'python_type': str },
      'GAP_pickled_ID': { 'type': 'string', 'python_type': str },
      'is_abelian': { 'type': 'boolean', 'python_type': bool },
      'is_cyclic': { 'type': 'boolean', 'python_type': bool },
      'is_simple': { 'type': 'boolean', 'python_type': bool },
      'is_nilpotent': { 'type': 'boolean', 'python_type': bool },
      'nilpotency_class': { 'type': 'number', 'python_type': int },
      'is_solvable': { 'type': 'boolean', 'python_type': bool },
      'derived_length': { 'type': 'number', 'python_type': int },
      'is_pgroup': { 'type': 'boolean', 'python_type': bool },
      'generators': { 'type': 'string', 'python_type': str },
      'char_degrees': { 'type': 'string', 'python_type': str },
      'D3': { 'type': 'number', 'python_type': int },
      'MBS_STPP_param_type': { 'type': 'array', 'python_type': tuple, 'length': 3 },
      'Beta0': { 'type': 'number', 'python_type': int }
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


    def __get_HTML_table_row( self ):

        row_line = ''

        while True:
            line = self.HTML_data_file.readline().lower()
            if not line == '':
                if '<tr>' in line:
                    row_line += line.replace( ' ', '' )
                    while True:
                        line = self.HTML_data_file.readline().lower()
                        if not line == '':
                            row_line += line.strip().replace( ' ', '' )
                            if '</tr>' in line:
                                return row_line
                            else: continue
                        else: break
            else: return 'EOF'

        return row_line


    def get_small_groups_HTML_data( self ):

        SmallGroup = collections.namedtuple(
                  'SmallGroup', TPPTripleDataParser.small_groups_JSON_schema.keys()
                                      )
        row = ''
        i = 0
        print '\n'
        row = self.__get_HTML_table_row()

        while not row == 'EOF':
            ID = self.__get_HTML_table_column_value( row, 'GAP_ID' )
            ptype = self.__get_HTML_table_column_value( row, 'MBS_STPP_param_type' )
            group_rec = SmallGroup( desc='', order=ID[0], GAP_ID=ID, GAP_desc='',
            GAP_pickled_ID='', is_abelian=None, is_cyclic=None, is_simple=None,
            is_nilpotent=None, nilpotency_class=None, is_solvable=None,
            derived_length=None, is_pgroup=None, generators=None,
            char_degrees=self.__get_HTML_table_column_value( row, 'char_degrees' ),
            D3=self.__get_HTML_table_column_value( row, 'D3' ),
            MBS_STPP_param_type=ptype, Beta0=ptype[0]*ptype[1]*ptype[2] )
            self.small_groups.update( {ID:group_rec} )
            i += 1
            row = self.__get_HTML_table_row()

        self.HTML_data_file.close()
        print 'Ordered dictionary of {} named tuples of small groups created.  File {} closed.'.format( len( self.small_groups ), self.HTML_data_file.name )


    def write_small_groups_JSON_file( self, file_dir, file_name, indent_num ):

        with io.open( file_dir + file_name, 'w', encoding='utf-8' ) as file:
            file.write( unicode( '[\n' ) )
            for count, small_group in enumerate( self.small_groups.values() ):
                if count:  file.write( unicode( ',\n' ) )
                JSON_obj = json.dumps( small_group._asdict(), \
                                       indent=indent_num, \
                                       ensure_ascii=False )
                file.write( unicode( JSON_obj ) )
            file.write( unicode( ']' ) )

        print '{} small group JSON objects successfully written to the file {}.'.\
              format( len( self.small_groups ), file.name )


    def read_small_groups_JSON_file( self, file_path ):

        sm_groups = collections.OrderedDict()
        decoder = json.JSONDecoder()

        with io.open( file_path, 'r', encoding='utf-8' ) as file:
            for line in file:
                if not '[\n' in line:
                    if '{' in line and '}' in line:
                        sm_group = decoder.raw_decode( line )[0]
                        ID = tuple( sm_group['GAP_ID'] )
                        sm_group['GAP_ID'] = ID
                        ptype = tuple( sm_group['MBS_STPP_param_type'] )
                        sm_group['MBS_STPP_param_type'] = ptype
                        sm_group = collections.namedtuple( 'SmallGroup', \
                                   TPPTripleDataParser.small_groups_JSON_schema.keys() )\
                                   ( **sm_group )
                        sm_groups.update( {ID:sm_group} )

        print 'Ordered dictionary of {} named tuples of small groups loaded from JSON file {}.'.format( len( sm_groups ), file.name )
        return sm_groups


    def __init__( self, file_path ):

        print 'Creating a new TPPTripleDataParser instance from file {}.'.\
              format( file_path )
        self.TPP_Triples = collections.OrderedDict()
        self.small_groups = collections.OrderedDict()
        self.HTML_data_file = open( file_path, 'r', 0 )
        self.small_groups_JSON_file = None
