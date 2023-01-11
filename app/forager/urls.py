from django.urls import path
from .views import (
    RecordListView,
    RecordCreateView,
    RecordDetailView,
    SpeciesListView,
    SpeciesDetailView,
    RecordUpdateView,
    RecordDeleteView
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", RecordListView.as_view(), name="home"),
    path("records/<int:pk>/", RecordDetailView.as_view(), name="record-detail"),
    path("records/new/", RecordCreateView.as_view(), name="record-create"),
    path("species/", SpeciesListView.as_view(), name="species"),
    path("species/<int:pk>/", SpeciesDetailView.as_view(), name="species-detail"),
    path('records/<int:pk>/update/', RecordUpdateView.as_view(), name='record-update'),
    path('records/<int:pk>/delete/', RecordDeleteView.as_view(), name='record-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
