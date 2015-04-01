from django import forms

class SmallGroupInfoForm( forms.Form ):
    small_group_ID = forms.CharField( label='Small Group GAP ID', max_length=14 )
