from django.db import models

# Create your models here.

class Banner(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/banner/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
