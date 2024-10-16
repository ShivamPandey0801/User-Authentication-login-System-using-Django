from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    status = models.BooleanField()

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.file.name