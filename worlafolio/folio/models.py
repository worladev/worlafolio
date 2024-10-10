from django.db import models

# Create your models here.
class BioData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    headline = models.CharField(max_length=150, blank=True)
    introduction = models.CharField(max_length=250, blank=True)
    profile_image = models.ImageField(upload_to='uploads/profile_pix', blank=True)
    resume = models.FileField(upload_to='uploads/resume/')

    def __str__(self):
        return self.first_name
    
