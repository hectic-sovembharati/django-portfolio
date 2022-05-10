from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class home(models.Model):
    name = models.CharField( max_length=50)
    profile = models.ImageField(null=True,blank=True,upload_to="images/")
    pa = models.TextField()
    foot = models.TextField()

class abou(models.Model):
    intro = models.TextField()
    
