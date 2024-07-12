from django import forms
from user.models import Child


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'last_name', 'date_of_birth', 'gender', 'short_description', 'picture',
                  'children_group']

class SearchChildForm(forms.Form):
    query = forms.CharField(label='Search for', max_length=100)
