'''
    Parser for the TPP triple raw data contained in static HTML tables located offline
    and online at http://www2.informatik.uni-halle.de/da/hedtke/tpp/
'''
class TPPTripleDataParser:

    def __init__( self, file_path ):
        print 'creating a new TPPTripleDataParser instance from file ' + str( file_path )
        self.TPP_Triples = []
        self.groups = []
        self.file = open( file_path, 'r', 0 )

    def get_data( self ):
        row = ''
        i = 0
        print '\n'
        while not row == 'EOF':
            row = self.get_row()
            group_tup = ( self.get_column_value( row, "group_GAP_ID" ),
                          self.get_column_value( row, "group_order" ),
                          self.get_column_value( row, "group_char_degrees" ),
                          self.get_column_value( row, "group_D3" ) )
            self.groups.append( group_tup )
            i += 1
        self.file.close()
        return self.groups

    def get_row( self ):
        row_line = ''
        while True:
            line = self.file.readline().lower()
            if not line == '':
                if '<tr>' in line:
                    row_line += line.strip()
                    while True:
                        line = self.file.readline().lower()
                        if not line == '':
                            row_line += line.strip()
                            if '</tr>' in line:
                                return row_line
                            else: continue
                        else: break
            else: return 'EOF'
        return row_line

    def get_column_value( self, row, col_name ):
        col_val = ''
        TD_indices = ()
        if col_name in [ 'group_GAP_ID', 'group_order' ]:
            TD_indices += self.get_TD_indices( row, 1 )
            if TD_indices != ():
                col_val = row[TD_indices[0]:TD_indices[1]]
            else: return 'ERROR'
            if col_name == 'group_GAP_ID':
                col_val = col_val.replace( '*', '' ).replace( ' ', '' )
            else:
                col_val = int( col_val.split( ',' )[0].replace( '[', '' ) )
        elif col_name == 'group_char_degrees':
            TD_indices += self.get_TD_indices( row, 2 )
            if TD_indices != ():
                col_val = row[TD_indices[0]:TD_indices[1]].replace( ' ', '' )
            else: return 'ERROR'
        elif col_name == 'group_D3':
            TD_indices += self.get_TD_indices( row, 3 )
            if TD_indices != ():
                col_val = int( row[TD_indices[0]:TD_indices[1]].replace( ' ', '' ) )
            else: return 'ERROR'
        return col_val

    def get_TD_indices( self, row, count ):
        i = j = 0
        while count > 0:
            i = row.find( '<td>', i + 1 )
            if i != -1: count -= 1
            else: return ()
        return (i + 4, row.find( '</td>', i ))







