from django.forms import ModelForm, widgets, ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Record
from leaflet.forms.widgets import LeafletWidget
import datetime


class CreateRecordModelForm(ModelForm):
    class Meta:
        model = Record
        template = "forager/record-create.html"
        fields = ["species", "date", "location", "notes", "private"]
        labels = {
            "species": _("Species"),
            "location": _("Enter location (WGS84) "),
            "note": _("Enter notes"),
            "private": _("Private record?"),
        }
        widgets = {"location": LeafletWidget(),
        "date": widgets.DateInput(attrs={'type': 'date'})}

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > datetime.date.today():  # 🖘 raise error if greater than
            raise ValidationError("The date cannot be in the future!")
        return date
