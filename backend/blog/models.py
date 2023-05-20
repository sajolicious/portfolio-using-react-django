from django.db import models
class blog(models.Model):
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=100)
  
class contact(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField(max_length=200)
  subject=models.CharField(max_length=200)
  message=models.CharField(max_length=200)