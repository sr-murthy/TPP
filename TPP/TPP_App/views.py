from django.http import HttpResponse

def welcome( request ):
    return HttpResponse( 'Welcome to the TPP app!' )

def small_group_info( request, GAP_ID ):
    return HttpResponse( 'Info request for small group with GAP ID {}'.format( GAP_ID ) )



