from django import forms
from .models import Specifications


class EditSpecificationsHeroForm(forms.ModelForm):

    class Meta:
        model = Specifications
        fields = ['named_item', 'furniture', 'engraving', 'evolution',
                  'hair', ]
        exclude = ['hero', 'user']

