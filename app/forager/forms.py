from django.forms import ModelForm, inlineformset_factory
from django.utils.translation import gettext, gettext_lazy as _
from .models import Record
from leaflet.forms.widgets import LeafletWidget

class CreateRecordModelForm(ModelForm):
    class Meta:
        model = Record
        template = 'forager/record-create.html'
        fields = ['species', 'notes', 'location', 'private']
        labels = {'species': _('Species'), 'note': _('Enter notes'), 'location': _('Enter location (WGS84) ')}
        widgets = {'location': LeafletWidget()}