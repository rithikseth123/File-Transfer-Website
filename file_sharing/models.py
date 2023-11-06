from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class SharedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    expiration_date = models.DateTimeField()
    unique_identifier = models.CharField(max_length=10, unique=True)
    def clean(self):
        super().clean()
        if self.file:
            # Check if file size is greater than 10MB
            if self.file.size > 500 * 1024 * 1024:  # 500MB in bytes
                raise ValidationError('File size cannot exceed 10MB.')
