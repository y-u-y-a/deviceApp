from django.db import models


# get upload path
def load_path(instance, filename):
    path = '/'.join([str(instance.title) + str('.jpg')])
    return path


class Device(models.Model):

    class Meta:
        db_table = 'device'

    title = models.CharField(max_length=30, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to=load_path)

    def __str__(self):
        return self.title

