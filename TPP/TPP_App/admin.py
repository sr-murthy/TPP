from django.contrib import admin
from TPP_App.models import SmallGroup

# Register your models here.
class SmallGroupAdmin( admin.ModelAdmin ):
    list_display = ( 'GAP_ID', 'GAP_desc', 'Beta0', 'MBS_STPP_param_type', 'D3' )

admin.site.register( SmallGroup, SmallGroupAdmin )
