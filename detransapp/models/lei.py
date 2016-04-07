from django.db import models

from detransapp.manager.lei import LeiManager


class Lei(models.Model):
    lei = models.CharField(max_length=50)
    objects = LeiManager()

    def __unicode__(self):
        return self.lei

    class Meta:
        app_label = "detransapp"
