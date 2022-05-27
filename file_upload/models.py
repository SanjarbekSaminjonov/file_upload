import os
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class FileQuerySet(models.QuerySet):

    def delete(self):
        for obj in self:
            os.remove(obj.file.path)
        super().delete()


class File(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField()
    file_name = models.CharField(max_length=255, blank=True)
    file_type = models.CharField(max_length=50, blank=True)
    file_size = models.CharField(max_length=50, blank=True)

    objects = FileQuerySet.as_manager()

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
        old_image_path = str()
        if self.file:
            self.file_name = self.file.name
            _, self.file_type = os.path.splitext(self.file.name)
            self.file_size = self.get_file_size()

            if self.pk:
                old_file_obj = File.objects.get(pk=self.pk)
                if old_file_obj.file != self.file:
                    old_image_path = old_file_obj.file.path

        super(File, self).save(*args, **kwargs)
        if old_image_path:
            os.remove(old_image_path)

    def delete(self, *args, **kwargs):
        if self.file:
            self.file.delete()

        super(File, self).delete(*args, **kwargs)
