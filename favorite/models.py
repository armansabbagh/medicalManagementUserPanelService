from django.db import models
from users.models import NormalUser,Doctor
# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(to=NormalUser,on_delete= models.CASCADE)
    doctor = models.ForeignKey(to=Doctor,on_delete=models.CASCADE)
