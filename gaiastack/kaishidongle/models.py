from django.db import models

# Create your models here.
class GaiaUser(models.Model):
    name = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)


    class Meta:
        db_table = 'gaiauser'

    def __unicode__(self):
        return self.name