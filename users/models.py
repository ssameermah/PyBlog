from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    # image = models.ImageField(default='default.jpg',upload_to ='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)
        
    #     img =Image.open(self.image.path)

    #     if img.height > 720 or img.width > 960:
    #         output_size = (720,960)

    #         img = Image.open(self.image.path)

    #         if img.height > 720 or img.width > 960:
    #             output_size = (720,960)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)
    
