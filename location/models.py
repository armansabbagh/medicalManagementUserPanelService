from django.db import models


# Create your models here.
class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = u'استان'
        verbose_name_plural = u'تمامی استان ها'

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(to=State, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = u'شهر'
        verbose_name_plural = u'تمامی شهرها'

    def __str__(self):
        return self.name
