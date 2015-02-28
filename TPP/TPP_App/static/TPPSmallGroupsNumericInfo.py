'''
    Utility class to provide numerical information about the GAP small groups which are included/excluded from the TPP project scope.
'''
import collections

class TPPSmallGroupsNumericInfo:

    excluded_TPP_small_groups = collections.OrderedDict( [ (128,[2320]), \
                                  (192,range( 1541, 1543)),(288,[1040,1044]), \
                                  (320,range( 1276, 1641 )),(324,[169, 175]), \
                                  (384,range( 1336,20170)),(432,'all'),(448,'all'), \
                                  (480,range( 824,1214 )),(486,range( 242,262 )), \
                                  (512,'all'),(544,'all'),(576,range( 520,8682 )), \
                                  (640,'all'),(648,range( 334,758 )), \
                                  (672,range( 684,1281 )),(686,[14]), \
                                  (704,range( 487,1388 )),(720,range( 473,841 )), \
                                  (729,range( 122,505)),(736,[194]), \
                                  (756,range( 172,190 )),(768,'all'), \
                                  (784,range( 132,173)),(800,range( 218,1212 )), \
                                  (810,range( 95, 114 )),(832,range( 298,1631 )), \
                                  (880,'all'),(896,'all'),(900,'all'),(912,'all'), \
                                  (928,'all'),(936,'all'),(960,'all'),(972,'all'), \
                                  (992,'all'),(1000,'all')] )

    GAP_small_groups_numeric_info = \
      GAPSmallGroupsNumericInfo.db


    @classmethod
    def exceptional_TPP_small_group_orders( cls ):

        return cls.excluded_TPP_small_groups.keys()


    @classmethod
    def is_exceptional_TPP_small_group_order( cls, order ):

        return order in cls.exceptional_TPP_small_group_orders()


    @classmethod
    def exceptional_TPP_small_group_indices_of_order( cls, order ):

        if order in cls.excluded_TPP_small_groups.keys():
            indices = cls.excluded_TPP_small_groups[order]
            if indices == 'all':
                return range( 1, cls.GAP_small_groups_numeric_info[order] + 1 )
            else:
                return indices
        else:
            return []

    @classmethod
    def is_exceptional_TPP_small_group( cls, ID ):

        return ID in [(ID[0],index) for index in \
                      cls.exceptional_TPP_small_group_indices_of_order( ID[0] )]


    @classmethod
    def num_exceptional_TPP_small_groups_in_ID_range( cls, ID1, ID2 ):

        return len( filter( lambda ID: cls.is_exceptional_TPP_small_group( ID ), \
                GAPSmallGroupsNumericInfo.GAP_small_group_IDs_in_range( ID1, ID2 ) ) )


    @classmethod
    def num_nonexceptional_TPP_small_groups_in_ID_range( cls, ID1, ID2 ):

        return len( filter( lambda ID: not cls.is_exceptional_TPP_small_group( ID ), \
                GAPSmallGroupsNumericInfo.GAP_small_group_IDs_in_range( ID1, ID2 ) ) )


    @classmethod
    def excluded_TPP_small_group_orders( cls ):

        return filter( lambda order: cls.excluded_TPP_small_groups[order] == 'all', \
                       cls.exceptional_TPP_small_group_orders() )


    @classmethod
    def is_excluded_TPP_small_group_order( cls, order ):

        return order in cls.excluded_TPP_small_group_orders()


    @classmethod
    def is_excluded_TPP_small_group( cls, ID ):

        if cls.is_exceptional_TPP_small_group_order( ID[0] ):
            if cls.is_excluded_TPP_small_group_order( ID[0] ):
                return True
            else:
                return ID[1] in cls.excluded_TPP_small_groups[ID[0]]

        return False


    @classmethod
    def num_excluded_TPP_small_groups_in_ID_range( cls, ID1, ID2 ):

        return len( filter( lambda ID: cls.is_excluded_TPP_small_group( ID ), \
                GAPSmallGroupsNumericInfo.GAP_small_group_IDs_in_range( ID1, ID2 ) ) )


    @classmethod
    def num_included_TPP_small_groups_in_ID_range( cls, ID1, ID2 ):

        return len( filter( lambda ID: not cls.is_excluded_TPP_small_group( ID ), \
                GAPSmallGroupsNumericInfo.GAP_small_group_IDs_in_range( ID1, ID2 ) ) )


    @classmethod
    def is_valid_TPP_small_group( cls, ID ):

        return not cls.is_excluded_TPP_small_group( ID ) and \
                   GAPSmallGroupsNumericInfo.is_valid_GAP_small_group_ID( ID )


    @classmethod
    def num_valid_TPP_small_groups_in_ID_range( cls, ID1, ID2 ):

        return len( filter( lambda ID: cls.is_valid_TPP_small_group( ID ), \
                GAPSmallGroupsNumericInfo.GAP_small_group_IDs_in_range( ID1, ID2 ) ) )


    @classmethod
    def num_invalid_TPP_small_groups_in_ID_range( cls, ID1, ID2 ):

        return len( filter( lambda ID: not cls.is_valid_TPP_small_group( ID ), \
                GAPSmallGroupsNumericInfo.GAP_small_group_IDs_in_range( ID1, ID2 ) ) )

