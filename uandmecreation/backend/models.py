from django.db import models
import datetime
# Create your models here.
class Banner(models.Model):
    banner = models.ImageField(upload_to = "banner_images",default = None,blank=True)
    name = models.TextField(default = None,blank=True)
    def __str__(self):
        return self.name
        
class HomePage(models.Model):
    Upcoming_events = models.TextField(default= "jun 30, 2020 15:37:25")
    Achieve_image = models.ImageField(upload_to = "frontend_images",default = None,blank=True)
    achieve = models.TextField(default = "Checklist Development and Management.")
    def __str__(self):
        return self.Upcoming_events
class Testimonial(models.Model):
    image = models.ImageField(upload_to = "testimonial_images",default = None,blank=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    description = models.TextField(default = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloret quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit.")
    def __str__(self):
        return self.name

class RecentPost(models.Model):
    image = models.ImageField(upload_to = "recent_posts",default = None,blank=True)
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=200,default= "jun 30, 2020 15:37:25")
    def __str__(self):
        return self.name
class Team(models.Model):
    image = models.ImageField(upload_to = "team_image",default = None,blank=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200,default= "Graphic Designer")
    def __str__(self):
        return self.name
class Gallery(models.Model):
    image = models.ImageField(upload_to = "Gallery_image",default = None,blank=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Event(models.Model):
    image = models.ImageField(upload_to = "event_image",default = None,blank=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=100,default= "06 aug")
    address = models.CharField(max_length=200)
    description = models.TextField(default = "It is a long established fact that a reader will be distracted by the readable.")
    def __str__(self):
        return self.name

class Slider(models.Model):
    image = models.ImageField(upload_to = "event_image",default = None,blank=True)
    date = models.CharField(max_length=100,default= "06 aug")
    def __str__(self):
        return self.date
class ContactUsDetail(models.Model):
    address = models.CharField(max_length=200,default= "206 South Marion Avenue, Indore")
    phone_no = models.CharField(max_length=20,default= "+1 (143) 456-7897")
    support_phone_no = models.CharField(max_length=20,default= "+1 (143) 456-7897")
    email = models.CharField(max_length=50,default='uandmecreation@gmail.com')
    def __str__(self):
        return self.address

