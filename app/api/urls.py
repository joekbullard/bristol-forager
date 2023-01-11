from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecordList, SpeciesListAPI, RecordDetail, api_root

urlpatterns = [
    path("records/", RecordList.as_view(), name="records-list-api"),
    path("species/", SpeciesListAPI.as_view(), name="species-list-api"),
    path("records/<int:pk>/", RecordDetail.as_view(), name="record-detail-api"),
    path("", api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
