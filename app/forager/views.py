from django.views import generic
from .models import Record, Species
from django.shortcuts import get_object_or_404
from django.contrib.gis.db import models


class RecordListView(generic.ListView):
    template_name = "forager/index.html"
    model = Record
    context_object_name = "records"

    def get_queryset(self):
        myset = {
            "first": Record.objects.order_by("-record_date")[:5],
            "second": Species.in_season.all(),
        }
        return myset


class RecordDetailView(generic.DetailView):

    model = Record
    template_name = "forager/record_detail.html"


class SpeciesListView(generic.ListView):
    template_name = "forager/species_list.html"
    model = Species
    context_obkect_name = "species"

class SpeciesDetailView(generic.DetailView):
    
    model = Species
    template_name = "forager/species_detail.html"


