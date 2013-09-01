from django.db import models

class KmeansCluster(models.Model):
    date = models.DateField()
    data = models.TextField(default='{}')

    def __unicode__(self):
        return "<date(%s)>"%(self.date, self.range)
