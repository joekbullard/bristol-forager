from django.contrib.gis.db import models
from users.models import CustomUser


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(" ", "_")
    return f"{name}/images/{filename}"


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(
        ImageAlbum, related_name="images", on_delete=models.CASCADE
    )


class Species(models.Model):
    """Species model."""

    common_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    description = models.TextField()
    forage_start = models.DateField(null=True)
    forage_end = models.DateField(null=True)
    album = models.OneToOneField(
        ImageAlbum, null=True, related_name="%(class)s_album", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["common_name"]
        verbose_name_plural = "species"

    def __str__(self):
        return self.common_name


class Record(models.Model):
    """Forage model."""

    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)
    album = models.OneToOneField(
        ImageAlbum, null=True, related_name="%(class)s_album", on_delete=models.CASCADE
    )
    location = models.PointField()

    class Meta:
        ordering = ["-record_date"]
        verbose_name_plural = "record"

    def __str__(self):
        return "%s - %s" % (self.species, self.record_date.date().strftime("%d-%m-%Y"))
