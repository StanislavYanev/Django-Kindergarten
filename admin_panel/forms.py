from django import forms

from admin_panel.models import Event
from user.models import Child


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'last_name', 'date_of_birth', 'gender', 'short_description', 'picture',
                  'children_group']

class SearchChildForm(forms.Form):
    query = forms.CharField(label='Search for', max_length=100)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'picture', 'venue', 'date', 'person_responsible', 'event_games','description']

