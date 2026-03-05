from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img=models.ImageField(default="profile-pics/locked.png",upload_to="profile-pics")
    
    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self):
        super().save()
        img=Image.open(self.profile_img.path)
        if img.height>300 and img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.profile_img.path)

