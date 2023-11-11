from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=100) 
    slug = models.SlugField(blank=True , null=True)
    email = models.EmailField()
    message = models.TextField() 
    
    class Meta:
        ordering = ['title']
        indexes = [ 
            models.Index(fields=['title']), 
            models.Index(fields=['slug']), 
        ]
