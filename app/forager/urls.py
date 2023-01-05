from django.urls import include, path
from .views import RecordListView, RecordCreateView, RecordDetailView, SpeciesListView, SpeciesDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("records/", RecordListView.as_view(), name="index"),
    path("records/<int:pk>/", RecordDetailView.as_view(), name="record-detail"),
    path("records/new/", RecordCreateView.as_view(), name="record-create"),
    path("species/", SpeciesListView.as_view(), name="species"),
    path("species/<int:pk>/", SpeciesDetailView.as_view(), name="species-detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
