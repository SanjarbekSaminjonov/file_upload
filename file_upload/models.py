import os
from django.db import models

# Create your models here.


class File(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=255, blank=True)
    file_type = models.CharField(max_length=50, blank=True)
    file_size = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.file_name

    def get_file_size(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1024, 2)
            ext = ' KB'
        else:
            value = round(x / 1048576, 2)
            ext = ' MB'
        return str(value) + ext

    def save(self, *args, **kwargs):

        if self.file:
            self.file_name, self.file_type = os.path.splitext(self.file.name)
            self.file_size = self.get_file_size()

        super(File, self).save(*args, **kwargs)
