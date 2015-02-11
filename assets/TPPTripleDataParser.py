import string

# create a subclass and override the handler methods
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
            i += 1
        self.file.close()

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

    def get_column_value( self, row, colName )
        columnVal = ''
        if colName == 'group_GAP_ID':
            TD_indices = get_TD_indices( row, 1 )
            columnVal = row[TD_indices[0]:TD_indices[1]]

    def get_TD_indices( row, count ):
        i = j = 0
        while count > 0:
            i = row.find( '<td>', i + 1 )
            if i != -1: count -= 1
            else: return -1
        return [i + 4, row.find( '</td>', i )]







