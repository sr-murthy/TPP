from django.db import models

class SmallGroup( models.Model ):

    GAP_ID = models.CommaSeparatedIntegerField( max_length=14, primary_key=True,\
                                                verbose_name="GAP small group ID" )
    order = models.IntegerField( null=False, verbose_name="Group order" )
    GAP_desc = models.CharField( max_length=100, null=False, \
                                 verbose_name="GAP structure description" )
    GAP_pickled_ID = models.CharField( max_length=250, null=True, \
                                 verbose_name="GAP IO pickled string representation" )
    index_LAN_subgroup = models.IntegerField( null=True,
      verbose_name="Index of a largest abelian normal subgroup" )
    index_LCN_subgroup = models.IntegerField( null=True,
      verbose_name="Index of a largest cyclic normal subgroup" )
    index_LEAN_subgroup = models.IntegerField( null=True,
      verbose_name="Index of a largest elementary abelian normal subgroup" )
    is_abelian = models.BooleanField( null=False, verbose_name="Abelian group?",\
                                      default=None )
    comm_length = models.IntegerField( null=False, verbose_name="Commutator length" )
    is_cyclic = models.BooleanField( null=False, verbose_name="Cyclic group?",\
                                     default=None )
    is_elem_abelian = models.BooleanField( null=False, \
                                 verbose_name="Elementary abelian group?",\
                                 default=None )
    is_simple = models.BooleanField( null=False, verbose_name="Simple group?",\
                                     default=None )
    comp_length = models.IntegerField( null=False, verbose_name="Composition length" )
    is_nilpotent = models.BooleanField( null=False, verbose_name="Nilpotent group?",\
                                        default=None )
    nilpotency_class = models.IntegerField( null=True, verbose_name="Nilpotency class" )
    is_solvable = models.BooleanField( null=False, verbose_name="Solvable group?",\
                                       default=None )
    derived_length = models.IntegerField( null=True, verbose_name="Derived length" )
    is_pgroup = models.BooleanField( null=False, verbose_name="Is p-group?",\
                                     default=None )
    generators = models.CharField( max_length=250, null=False, \
                                   verbose_name="Generators and orders" )
    char_degrees = models.CharField( max_length=250, null=False, \
                                   verbose_name="Character degrees and multiplicities" )
    D3 = models.IntegerField( null=False, \
                              verbose_name="Sum of cubes of character degrees (D3)" )
    MBS_STPP_param_type = models.CommaSeparatedIntegerField( max_length=16, null=False, \
                    verbose_name="Maximum-by-size (MBS) subgroup TPP (STPP) triple type" )
    Beta0 = models.IntegerField( null=False, verbose_name="Subgroup TPP capacity (B0)" )

    def get_GAP_ID_asstring( self ):

        return self.GAP_ID.join( '[]' )

    def get_GAP_ID_asnumeric( self ):

        return [int( token.strip( ' ' ) ) for token in self.GAP_ID.split( ',' )]

    def get_MBS_STPP_param_type_asstring( self ):

        return self.MBS_STPP_param_type.join( '()' )

    # returns a numeric tuple for MBS_STPP_param_type
    def get_MBS_STPP_param_type_asnumeric( self ):

        return tuple( [int( token.strip( ' ' ) ) \
                       for token in self.MBS_STPP_param_type.split( ',' )] )

