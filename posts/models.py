from django.db import models

# Create your models here.


class Post(models.Model):
    objects = models.Manager()

    text = models.TextField()

    def __str__(self):
        # строковое отображение модели
        return self.text[:50]


