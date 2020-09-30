from django.db import models

# Create your models here.
class data(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.IntegerField()
    end = models.IntegerField()
    iri = models.DecimalField(max_digits = 10, decimal_places=10)