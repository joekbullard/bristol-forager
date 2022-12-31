from django.views import generic
from .models import Record, Species

class IndexView(generic.ListView):
    template_name = "forager/index.html"
    context_object_name = "record_list"

    def get_queryset(self):
        myset = {
            "first": Record.objects.order_by("-record_date")[:5],
            "second": Species.in_season.all(),
        }
        return myset
