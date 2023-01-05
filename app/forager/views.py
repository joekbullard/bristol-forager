from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Record, Species
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateRecordModelForm
from django.core.serializers import serialize
from django.http import HttpResponse
import json


class RecordListView(ListView):
    template_name = "forager/index.html"
    model = Record
    context_object_name = "records"

    def get_queryset(self):
        myset = {
            "first": Record.objects.order_by("-record_date")[:5],
            "second": Species.in_season.all(),
        }
        return myset


class RecordDetailView(DetailView):

    model = Record
    template_name = "forager/record_detail.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super(RecordDetailView, self).get_context_data(**kwargs)
        # this serializer formats geojson incorrectly - adding a crs key
        record_json = json.loads(serialize("geojson", Record.objects.filter(id=self.kwargs['pk']), geometry_field='location'))
        # load as python json object and remove crs from json
        record_json.pop('crs', None)
        context['data'] = record_json

        return context



class RecordCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateRecordModelForm
    model = Record
    template_name = "forager/record-create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #fields = ['species', 'notes', 'location', ]



    


class SpeciesListView(ListView):
    template_name = "forager/species_list.html"
    model = Species
    context_obkect_name = "species"

class SpeciesDetailView(DetailView):
    
    model = Species
    template_name = "forager/species_detail.html"


