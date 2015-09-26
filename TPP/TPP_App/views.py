from django.http import HttpResponse

from .models import SmallGroup

def welcome( request ):
    return HttpResponse( 'Welcome to the TPP app!' )

# The GAP_ID argument must be a string in the form 'X, Y' where X is the order of the group
# and Y is the index of this group in the collection of GAP small groups of this order.
# e.g. GAP_ID = '6, 1' refers to the symmetric group of order 3! = 6, commonly denoted as Sym_3.
def small_group_info( request, GAP_ID ):
    return HttpResponse( SmallGroup.objects.get( GAP_ID=GAP_ID.replace(',', ', ') ) )



