from django.db import models
from users.models import NormalUser, Doctor


# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    doctor = models.ForeignKey(to=Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(to=NormalUser, on_delete=models.CASCADE)
