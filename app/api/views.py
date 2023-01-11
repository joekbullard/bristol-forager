from django.views import generic
from forager.models import Record, Species
from rest_framework import generics, permissions
from .serializers import RecordSerializer, SpeciesSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view  # new
from rest_framework.response import Response  # new
from rest_framework.reverse import reverse  # new


@api_view(["GET"])  # new
def api_root(request, format=None):
    return Response(
        {"records": reverse("records-list-api", request=request, format=format)}
    )


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class SpeciesListAPI(generics.ListCreateAPIView):
    queryset = Species.objects.all()

    serializer_class = SpeciesSerializer

    def perform_create(self, serializer):  # new
        serializer.save(owner=self.request.user)
