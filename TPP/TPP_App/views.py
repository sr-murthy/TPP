from django.http import HttpResponse

from TPP_App.models import SmallGroup

def welcome( request ):
    return HttpResponse( 'Welcome to the TPP app!' )

def small_group_info( request, ID ):
    return HttpResponse( SmallGroup.objects.get( GAP_ID='6, 1' ) )



