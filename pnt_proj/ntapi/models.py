from django.db import models

# Species class
class Species(models.Model):
    id                  = models.IntegerField(primary_key=True, blank=False, editable=False)
    common_name         = models.CharField(max_length=150, null = True)
    species             = models.CharField(max_length=150, unique=True, null = True)
    family              = models.CharField(max_length=100, null = True)
    ecological_classification   = models.CharField(max_length=50, null = True)
    conservation_status         = models.CharField(max_length=50, null = True)
    binhi_priority         = models.CharField(max_length=3, null = True)
    # min_altitude        = models.IntegerField(default=0) 
    # max_altitude        = models.IntegerField(default=0)
    # alay_page           = models.IntegerField(default=0)