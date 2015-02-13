'''
    Parser for the TPP triple raw data contained in static HTML tables located offline,
    and online at http://www2.informatik.uni-halle.de/da/hedtke/tpp/
'''
import collections

class TPPTripleDataParser:

    groups_JSON_fields = ['desc', 'order', 'GAP_ID', 'GAP_desc', 'GAP_pickled_ID', 'is_abelian', 'is_cyclic', 'is_simple', 'is_nilpotent', 'nilpotency_class', 'is_solvable', 'derived_length', 'is_pgroup', 'generators', 'char_degrees', 'D3', 'MBS_STPP_param_type', 'Beta0']

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
            line = self.file.readline().lower()
            if not line == '':
                if '<tr>' in line:
                    row_line += line.replace( ' ', '' )
                    while True:
                        line = self.file.readline().lower()
                        if not line == '':
                            row_line += line.strip().replace( ' ', '' )
                            if '</tr>' in line:
                                return row_line
                            else: continue
                        else: break
            else: return 'EOF'

        return row_line


    def get_groups_data( self ):

        Group = collections.namedtuple( 'Group', TPPTripleDataParser.groups_JSON_fields )
        row = ''
        i = 0
        print '\n'
        row = self.__get_HTML_table_row()

        while not row == 'EOF':
            ID = self.__get_HTML_table_column_value( row, 'GAP_ID' )
            ptype = self.__get_HTML_table_column_value( row, 'MBS_STPP_param_type' )
            group_rec = Group( desc='', order=ID[0], GAP_ID=ID, GAP_desc='',
            GAP_pickled_ID='', is_abelian=None, is_cyclic=None, is_simple=None,
            is_nilpotent=None, nilpotency_class=None, is_solvable=None,
            derived_length=None, is_pgroup=None, generators=None,
            char_degrees=self.__get_HTML_table_column_value( row, 'char_degrees' ),
            D3=self.__get_HTML_table_column_value( row, 'D3' ),
            MBS_STPP_param_type=ptype, Beta0=ptype[0]*ptype[1]*ptype[2] )
            self.groups.update( {ID:group_rec} )
            i += 1
            row = self.__get_HTML_table_row()
        self.file.close()
        print 'Ordered dictionary of ' + str( len( groups ) ) + ' named tuples of groups created.  File ' + self.file.name + ' closed.'


    def __format_groups_JSON_record_line( self, field, value ):

        record_line = ''
        record_line += ' '*4 + '"' + field + '": '
        if field in [ 'desc', 'GAP_desc', 'GAP_pickled_ID', \
                      'generators', 'char_degrees' ]:
            if value != None: record_line += str( value ).join( '""' )
            else: record_line += 'null'
        elif field in [ 'order', 'is_abelian', 'is_cyclic', 'is_simple', \
                                'is_nilpotent', 'nilpotency_class', 'is_solvable', \
                                'derived_length', 'is_pgroup', 'D3', 'Beta0' ]:
            if value != None: record_line += str( value )
            else: record_line += 'null'
        elif field in [ 'GAP_ID', 'MBS_STPP_param_type' ]:
            if value != None: record_line += str( list( value ) )
            else: record_line += 'null'
        if fields.index( field ) != len( fields ) - 1:
            record_line += ','

        return record_line


    def __format_groups_JSON_record( self, group ):

        fields = group._fields
        record = ''

        record += ' '*2 + '{\n'
        for field in fields:
            value = group[fields.index( field )]
            record_line = self.__format_groups_JSON_record_line( field, value )
            record += record_line + '\n'
            record_line = ''
        record += ' '*2 + '}'

        return record


    def write_groups_JSON_file( self, file_dir, file_name ):

        file = open( file_dir + file_name, 'w' )
        record = ''

        file.write( '{\n' )
        i = 0
        for ID in self.groups.keys():
            if i > 0:
                record = '\n'
            record += self.__format_groups_JSON_record( self.groups[ID] )
            if i != len( groups ) - 1: record += ','
            file.write( record )
            i += 1
        file.write( ' '*2 + '\n}' )

        file.close()
        print str( i ) + ' JSON records successfully written to the file ' + \
              file.name + '.'


    def __init__( self, file_path ):

        print 'Creating a new TPPTripleDataParser instance from file ' + \
              str( file_path ) + '.'
        self.TPP_Triples = collections.OrderedDict()
        self.groups = collections.OrderedDict()
        self.file = open( file_path, 'r', 0 )
        self.groups_JSON_file = None


