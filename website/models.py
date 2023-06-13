from django.db import models

# Create your models here.
# models.py
from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_file_size(self):
        if self.file:
            return self.file.size
        return None
