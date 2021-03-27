from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, 'admin'),
        (1, 'normal_user'),
        (2, 'doctor'),
    )

    username = models.CharField(primary_key=True, max_length=50, verbose_name='نام کاربری', null=False, blank=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='normal_user_info')
    birth_date = models.DateField(verbose_name=u'تاریخ تولد', blank=True, null=True)
    national_code = models.CharField(max_length=11, verbose_name=u'کد ملی', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name=u'شماره تلفن')
    home_phone = models.CharField(max_length=15, verbose_name=u'شماره تلفن منزل', blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name=u'آدرس', blank=True, null=True)
    disease = models.CharField(max_length=30, verbose_name=u'بیماری')
    disease_detail = models.CharField(max_length=300, verbose_name='جزئیات بیماری', blank=True, null=True)

    class Meta:
        verbose_name = u'کاربر عادی'
        verbose_name_plural = u'کاربران عادی'

    def __str__(self):
        return self.user.last_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor_info')
    specialist_type = models.CharField(max_length=50, verbose_name='تخصص')
    content = models.TextField(max_length=500, verbose_name='توضیحات', blank=True, null=True)
    work_address = models.CharField(max_length=100, verbose_name=u'آدرس مطب')
    work_phone = models.CharField(max_length=15, verbose_name=u'شماره تلفن مطب')

    class Meta:
        verbose_name = u'پزشک'
        verbose_name_plural = u'پزشکان'

    def __str__(self):
        return self.user.first_name + self.user.last_name
