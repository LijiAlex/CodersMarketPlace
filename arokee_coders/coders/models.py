from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Coder(models.Model):

    category_choices = (
        ('full_stack', 'full stack'),
        ('fornt_end', 'front end'),
        ('back_end', 'back end'),
        ('web_development', 'web development'),
        ('data_analysis', 'data analysis'),
        ('dev_ops', 'dev ops')
    )
        
    type = (
        ('company', 'company'),
        ('individual', 'individual'),
        ('team', 'team')
    )

    name = models.CharField( max_length = 255)
    hourly_rate = models.IntegerField()
    commit_hours = models.IntegerField()
    hired = models.IntegerField(default=0)
    skill_set = models.CharField( max_length = 255)
    category = models.CharField(choices=category_choices, max_length = 255)
    type = models.CharField(choices=type, max_length = 255)
    description = models.TextField()
    video_intro = models.CharField( max_length = 255)
    work_history = RichTextField()
    github_link = models.CharField( max_length = 255)
    linkedin_link = models.CharField( max_length = 255)
    portfolio_link = models.CharField( max_length = 255)
    city = models.CharField( max_length = 255)
    is_featured = models.BooleanField(default=False)
    photo = models.ImageField(upload_to= "media/coders/%Y/%m/")
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name





