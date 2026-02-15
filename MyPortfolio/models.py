from django.db import models
from django.contrib.auth.models import User



class portfolios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Hero section
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    github = models.URLField(blank=True)      
    linkedin = models.URLField(blank=True)                     

    # About section
    about = models.TextField(blank=True)
    skills = models.TextField(blank=True)  # can store comma-separated skills

    # Projects section
    
    # Services section
    services = models.TextField(blank=True)  # optional list of services

    def __str__(self):
        return self.full_name


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    

    def __str__(self):
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null if currently working
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} at {self.company}"