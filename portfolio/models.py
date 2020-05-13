from django.db import models

class Project(models.Model):     #https://docs.djangoproject.com/en/3.0/ref/models/fields/
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title  #shows the tile in admin of the project