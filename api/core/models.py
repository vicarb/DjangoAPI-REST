from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
        
class Negocio(models.Model):
    title = models.CharField(max_length=255)
    negocio_slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name="negocios", on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.title
