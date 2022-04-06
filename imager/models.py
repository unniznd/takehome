from django.db import models
from django.contrib.auth.models import User

import uuid

#upload image with unique name according to user
def userPath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '{0}/{1}'.format(instance.user.id, filename)

class Imager(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=userPath)
