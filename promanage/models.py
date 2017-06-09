from django.db import models

from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "%s/thumbnail/%s" % (instance.user, filename)
class Property(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    proname = models.CharField('Name',max_length=50)
    PROPERTY_TYPE_CHOICES = (
        ('HOUSE','HOUSE'),
        ('LAND','LAND'),
        ('APARTMENT','APARTMENT'),
    )
    PLAN_CHOICES=(
        ('SILVER','SILVER'),
        ('GOLD', 'GOLD'),
        ('DIAMOND', 'DIAMOND'),
    )
    SERVICE_TYPE_CHOICES =(
        ('RENTAL','RENTAL'),
        ('SALE', 'SALE'),
        ('MAINTENANCE', 'MAINTENANCE'),
        ('CONSTRUCTION', 'CONSTRUCTION'),
    )
    property_type = models.CharField(
        max_length=10,
        choices=PROPERTY_TYPE_CHOICES,
        default='HOUSE'
    )
    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_TYPE_CHOICES,
        default='MAINTENANCE'
    )
    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        default='SILVER'
    )
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to=upload_location, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
    def __str__(self):
            return self.user.username

class Notification(models.Model):
    to_user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField('content')
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta :
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __str__(self):
        return self.to_user.username