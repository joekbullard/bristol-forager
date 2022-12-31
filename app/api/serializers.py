from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from forager.models import Record, ImageRecord, Species, ImageSpecies


class ImageRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRecord
        fields = ("id", "image", "default")


class RecordSerializer(GeoFeatureModelSerializer):
    record_images = ImageRecordSerializer(many=True)
    species = serializers.StringRelatedField()
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Record
        geo_field = "location"

        fields = ("id", "species", "user", "record_date", "notes", "record_images")


class ImageSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSpecies
        fields = ("id", "image", "caption", "default")


class SpeciesSerializer(serializers.ModelSerializer):
    species_images = ImageSpeciesSerializer(many=True)

    class Meta:
        model = Species
        fields = (
            "id",
            "common_name",
            "scientific_name",
            "description",
            "start",
            "end",
            "species_images",
        )
