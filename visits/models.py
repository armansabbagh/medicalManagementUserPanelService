from django.db import models
from users.models import Doctor, NormalUser


# Create your models here.
class VisitTime(models.Model):
    date = models.DateField(verbose_name=u'تاریخ نوبت')
    time = models.TimeField(verbose_name=u'زمان نوبت')
    doctor = models.ForeignKey(to=Doctor, on_delete=models.CASCADE, verbose_name=u'دکتر معالج')
    patient = models.ForeignKey(to=NormalUser, on_delete=models.CASCADE, null=True, verbose_name=u'بیمار')

    def __str__(self):
        return "doctor : " + self.doctor.user.username+" / date: "+self.date.__str__() +" / time: "+ self.time.__str__()