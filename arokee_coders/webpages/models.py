from django.db import models

# Create your models here.

class Banner(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/banner/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline 

class TeamMember(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/%m')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name 
