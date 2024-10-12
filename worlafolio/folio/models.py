from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    cell_phone1 = PhoneNumberField(unique=True, blank=True)
    headline = models.CharField(max_length=150, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    introduction = models.TextField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='profile_pix/', blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)

    class Meta:
        verbose_name = 'biodata'
        verbose_name_plural = 'biodata'

    def __str__(self):
        return self.first_name
    

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='project_image/', blank=True)
    technologies = models.CharField(max_length=100)
    project_url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    school_name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True, blank=True)



class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    organization = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True, blank=True)
    position_held = models.CharField(max_length=100)
    duties = models.CharField(max_length=200)

    def __str__(self):
        return self.position_held
    
