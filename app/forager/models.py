from django.contrib.gis.db import models
from users.models import CustomUser
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(" ", "_")
    return f"/images/{filename}"
    

class SpeciesInSeasonManager(models.Manager):
    def get_queryset(self):
        today = timezone.now().month
        return super(SpeciesInSeasonManager, self).get_queryset().filter(start__month__lte=today, end__month__gte=today)


class Species(models.Model):
    """Species model."""

    common_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateField(null=True)
    end = models.DateField(null=True)

    objects = models.Manager() # The default manager.
    in_season = SpeciesInSeasonManager() # New manager

    '''
    def in_season(self):
        return self.start <= timezone.now() <= self.end 
    '''
    class Meta:
        ordering = ["common_name"]
        verbose_name_plural = "species"

    def __str__(self):
        return self.common_name


class ImageSpecies(models.Model):
    species = models.ForeignKey(Species, related_name='species_images', on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "image species"


class Record(models.Model):
    """Record model."""

    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)
    private = models.BooleanField(default=False)
    location = models.PointField()

    class Meta:
        ordering = ["-record_date"]
        verbose_name_plural = "record"

    def __str__(self):
        return "%s - %s" % (self.species, self.record_date.date().strftime("%d-%m-%Y"))

    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.pk})


class ImageRecord(models.Model):
    record = models.ForeignKey(Record, related_name='record_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    default = models.BooleanField(default=False)
