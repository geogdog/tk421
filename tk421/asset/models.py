from django.db import models

class Location(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Asset(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label
