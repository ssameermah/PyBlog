from django.db import models
from django.utils import timezone #imported so that we can use timezone.now in date by which we can update the time of the post
from django.contrib.auth.models import User #to get the default django auth_user table
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now) #time and date can be updated
    link = models.URLField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #models.CASCADE; if user is deleted all this posts will be delted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    