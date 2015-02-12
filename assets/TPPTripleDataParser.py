'''
    Parser for the TPP triple raw data contained in static HTML tables located offline,
    and online at http://www2.informatik.uni-halle.de/da/hedtke/tpp/
'''
import collections

class TPPTripleDataParser:

    def __init__( self, file_path ):
        print 'creating a new TPPTripleDataParser instance from file ' + str( file_path )
        self.TPP_Triples = collections.OrderedDict()
        self.groups = collections.OrderedDict()
        self.file = open( file_path, 'r', 0 )
        self.groups_data_file = None

    def get_groups_data( self ):
        Group = collections.namedtuple( 'Group', 'desc order GAP_ID GAP_desc GAP_pickled_ID is_abelian is_cyclic is_simple is_nilpotent nilpotency_class is_solvable derived_length is_pgroup generators char_degrees D3 MBS_STPP_param_type Beta0' )
        row = ''
        i = 0
        print '\n'
        row = self.get_row()
        while not row == 'EOF':
            ID = self.get_column_value( row, "GAP_ID" )
            ptype = self.get_column_value( row, "MBS_STPP_param_type" )
            group_rec = Group( desc='', order=ID[0], GAP_ID=ID, GAP_desc='',
            GAP_pickled_ID='', is_abelian=None, is_cyclic=None, is_simple=None,
            is_nilpotent=None, nilpotency_class=None, is_solvable=None,
            derived_length=None, is_pgroup=None, generators=None,
            char_degrees=self.get_column_value( row, "char_degrees" ),
            D3=self.get_column_value( row, "D3" ),
            MBS_STPP_param_type=ptype, Beta0=ptype[0]*ptype[1]*ptype[2] )
            self.groups.update( {ID:group_rec} )
            i += 1
            row = self.get_row()
        self.file.close()
        return self.groups

    def get_row( self ):
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

    def get_column_value( self, row, col_name ):
        col_val = ''
        col_indices = ()
        if col_name in [ 'GAP_ID', 'order' ]:
            col_indices += self.get_column_indices( row, 1 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].translate( None, '[]* ' )
                col_val = tuple( int( s ) for s in col_val.split( ',' ) )
            else: return 'ERROR'
            if col_name == 'order': col_val = col_val[0]
        elif col_name == 'char_degrees':
            col_indices += self.get_column_indices( row, 2 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].replace( ' ', '' )
            else: return 'ERROR'
        elif col_name == 'D3':
            col_indices += self.get_column_indices( row, 3 )
            if col_indices != ():
                col_val = int( row[col_indices[0]:col_indices[1]].replace( ' ', '' ) )
        elif col_name in [ 'MBS_STPP_param_type', 'Beta0' ]:
            col_indices += self.get_column_indices( row, 9 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].replace( ' ', '' )
                col_val = [int( s ) for s in col_val.split( ',' )]
                col_val.reverse()
                col_val = tuple( col_val )
                if col_name == 'Beta0':
                    col_val = col_val[0]*col_val[1]*col_val[2]
        else: return 'ERROR'

        return col_val

    def get_column_indices( self, row, count ):
        i = j = 0
        while count > 0:
            i = row.find( '<td>', i + 1 )
            if i != -1: count -= 1
            else: return ()
        return (i + 4, row.find( '</td>', i ))
