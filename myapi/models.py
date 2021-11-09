from django.db import models

# Create your models here.

class Document(models.Model):
    version_no = models.IntegerField(unique=True, null=True, blank=True)
    upload_type = models.TextField(max_length=100)
    attachment = models.FileField(null=True, blank=True)
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}'
    
        
class DocAttach(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}'
    