from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IndexView, RecordList, SpeciesListAPI, RecordDetail, api_root

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/records/', RecordList.as_view(), name='records-list'),
    path('api/species/', SpeciesListAPI.as_view(), name='species-list'),
    path('api/records/<int:pk>/', RecordDetail.as_view(), name='record-detail'),
    path('api/', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
