from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    instrument = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name +" "+ self.last_name