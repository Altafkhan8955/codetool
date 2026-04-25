from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    comment = models.TextField()
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
class ClientQuery(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    message = models.TextField()
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
class Service(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="serviceimg/")
    link = models.CharField(max_length=255, null=True)
#backgorond remove image model
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')     
#image resize by mb to kb
class ResizableImage(models.Model):
    original_image = models.ImageField(upload_to='images/')   
#image resize by height and width
class ResizedImage(models.Model):
    image = models.ImageField(upload_to='resize/')
#convert image format jpg to png   
class ConvertpngModel(models.Model):
    image = models.ImageField(upload_to='covertpng/')
    
#convert image format jpg
class ConvertjpgModel(models.Model):
    image = models.ImageField(upload_to='convertjpg/')
class SiteMaps(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    







