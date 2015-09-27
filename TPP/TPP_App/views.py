from django.http import HttpResponse

from .models import SmallGroup
from .lib import TPPSmallGroupsNumericInfo, GAPSmallGroupsNumericInfo

def welcome( request ):
    return HttpResponse( 'Welcome to the TPP app!' )

# The GAP_ID argument must be a string in the form 'X,Y' where X is the order of the group
# and Y is the index of this group in the collection of GAP small groups of this order.
# e.g. GAP_ID = '6,1' refers to the symmetric group of order 3! = 6, commonly denoted as
# Sym_3.
#
# Note 1: in GAP itself small group IDs are displayed in the format '[ X, Y ]', where 'X'
# and 'Y' are as described above.
#
# Note 2: in the TPP app database GAP IDs are stored in the small groups table in the
# string format 'X, Y', and are displayed in the format '[X, Y]'.
def small_group_info( request, GAP_ID ):

	GAP_ID_numeric = tuple([int(t1) for t1 in GAP_ID.split(',')])
	if TPPSmallGroupsNumericInfo.is_valid_TPP_small_group( GAP_ID_numeric ):
		return HttpResponse( SmallGroup.objects.get( GAP_ID=GAP_ID.replace(',', ', ') ) )
	else:
		if not GAPSmallGroupsNumericInfo.is_valid_GAP_small_group_ID( GAP_ID_numeric ):
			return HttpResponse( '{} is not a valid GAP small group.  Please refer to http://www.gap-system.org/Packages/sgl.html for more information.'.format( GAP_ID.replace(',', ', ').join('[]') ) )
		else:
			return HttpResponse( 'The GAP small group {} is excluded from the original TPP triple search dataset.  Please refer to http://www2.informatik.uni-halle.de/da/hedtke/tpp/README.txt for more information.'.format( GAP_ID.replace(',', ', ').join('[]') ) )



