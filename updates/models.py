from django.conf import settings
from django.db import models

# Create your models here.


def upload_update_image(instance, filename):
    return 'updates/{user}/{filename}'.format(user=instance.user, filename)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blacnk=True, null=True)
    image = models.ImageField(
        upload_to=upload_update_image, blacnk=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""
