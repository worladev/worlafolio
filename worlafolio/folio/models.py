from django.db import models

# Create your models here.
class BioData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    headline = models.CharField(max_length=150, blank=True)
    introduction = models.TextField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='uploads/profile_pix/', blank=True)
    resume = models.FileField(upload_to='uploads/resume/', blank=True)

    class Meta:
        verbose_name = 'biodata'
        verbose_name_plural = 'biodata'

    def __str__(self):
        return self.first_name
    

class Projects(models.Model):
    title = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='uploads/project_image', blank=True)
    technologies = models.CharField(max_length=100)
    project_url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title


class Education(models.Model):
    school_name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True, blank=True)
