from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ethics_agreed = models.IntegerField(default=0)
    age_range = models.IntegerField(default=0)
    gender = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Incident(models.Model):
    status = models.IntegerField(default=0)
    details = models.CharField(max_length=4096)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    date = models.DateTimeField()
    user = models.ForeignKey(User, null=True, blank=True, default = None)
    def __unicode__(self):
        return str(self.lat)+", "+str(self.lon)

class IncidentImage(models.Model):
    status = models.IntegerField(default=0)
    incident = models.ForeignKey(Incident)
    image = models.ImageField(default=0)
    def __unicode__(self):
        return self.incident.__unicode__()
