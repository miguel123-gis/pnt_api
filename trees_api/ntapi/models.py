from django.db import models
import uuid

# Choices for ecological classification
ECOLOGICAL_CLASSIFICATION = [('IN', 'Indigenous'), ('EN', 'Endemic')]

# Choices for conservation status
CONSERVATION_STATUS = [
    ('CR', 'Critically Endangered'),
    ('DD', 'Data Deficient'),
    ('EN', 'Endangered'),
    ('LC', 'Least Concern'),
    ('NE', 'Not Evaluated'),
    ('NT', 'Near Threatened'),
    ('OWS', 'Other Wildife Species'),
    ('OTS', 'Other Threatened Species'),
    ('VU', 'Vulnerable')
]

# Species class
class Species(models.Model):
    common_name         = models.CharField(max_length=50)
    species             = models.CharField(max_length=50)
    # family              = models.CharField(max_length=50)
    # common_name_other   = models.CharField(max_length=50)
    # min_altitude        = models.IntegerField(default=0) 
    # max_altitude        = models.IntegerField(default=0)
    # ecological_classification   = models.CharField(max_length=50, choices=ECOLOGICAL_CLASSIFICATION)
    # conservation_status         = models.CharField(max_length=50, choices=CONSERVATION_STATUS)
    # alay_page           = models.IntegerField(default=0)