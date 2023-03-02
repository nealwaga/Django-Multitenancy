from django.db import models

# Create your models here.
class Students(models.Model):
    registration_number = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.registration_number