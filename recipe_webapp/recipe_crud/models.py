from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    author =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    direction = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('recipe_crud:detail',
        kwargs={'pk':self.pk})