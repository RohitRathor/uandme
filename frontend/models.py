from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    venue = models.CharField(max_length=200,default = None)
    message = models.TextField(max_length=500,default = None)
    mobile = models.CharField(max_length=15,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name