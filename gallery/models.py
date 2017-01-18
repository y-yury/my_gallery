from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


#Ensuring image validation is performed on upload
def image_validation(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    upload_limit = 2.0
    if filesize > upload_limit*1024*1024:
        raise ValidationError("Sorry, maximum filesize allowed is {}Mb.".format(upload_limit))


class Photo(models.Model):
    author = models.OneToOneField(User, unique=True, null=True)
    title = models.CharField(max_length=250, null=True)
    width = models.IntegerField(default=0, null=True)
    height = models.IntegerField(default=0, null=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False, width_field="width", height_field="height",
                              validators=[image_validation])
    timestamp = models.DateTimeField(default=timezone.now, auto_now=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]