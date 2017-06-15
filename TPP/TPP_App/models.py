from django.db import models

class SmallGroup( models.Model ):

    GAP_ID = models.CommaSeparatedIntegerField( max_length=14, primary_key=True,\
                                                verbose_name="GAP small group ID" )
    ordr = models.IntegerField( null=False, verbose_name="Group order" )
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

    @property
    def GAP_ID_string( self ):

        return self.GAP_ID.join( '[]' )

    @property
    def GAP_ID_numeric( self ):

        return tuple([int( token.strip( ' ' ) ) for token in self.GAP_ID.split( ',' )])

    @property
    def GAP_ID_TPPApp_format(self):
 
        return self.GAP_ID.join('[]')

    @property
    def MBS_STPP_param_type_string( self ):

        return self.MBS_STPP_param_type.join( '()' )

    # returns a numeric tuple for MBS_STPP_param_type
    @property
    def MBS_STPP_param_type_numeric( self ):

        return tuple( [int( token.strip( ' ' ) ) \
                       for token in self.MBS_STPP_param_type.split( ',' )] )

    # returns the subgroup TPP ratio of this group - the formula is (group Beta0 / group order)
    @property
    def rho0( self ):

        return float( self.Beta0 ) / self.ordr

    def __unicode__( self ):

        return 'GAP ID: {}, GAP structure description: {}, order: {}, index of a largest abelian normal (LAN) subgroup: {}, index of a largest cyclic normal (LCN) subgroup: {}, index of a largest elementary abelian normal (LEAN) subgroup: {}, is abelian: {}, commutator length: {}, is cyclic: {}, is elementary abelian: {}, is simple: {}, composition length: {}, is nilpotent: {}, nilpotency class: {}, is solvable: {}, derived length: {}, is p-group: {}, generators and orders: {}, character degrees and multiplicities: {}, sum of cubes of character degrees (D3): {}, maximal-by-size(MBS) subgroup TPP (STPP) triple type: {}, subgroup TPP capacity (B0): {} \n'.format( self.GAP_ID_string, self.GAP_desc, self.ordr, self.index_LAN_subgroup, self.index_LCN_subgroup, self.index_LEAN_subgroup, self.is_abelian, self.comm_length, self.is_cyclic, self.is_elem_abelian, self.is_simple, self.comp_length, self.is_nilpotent, self.nilpotency_class, self.is_solvable, self.derived_length, self.is_pgroup, self.generators, self.char_degrees, self.D3, self.MBS_STPP_param_type_string, self.Beta0 )

