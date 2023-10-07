from django.db import models
from embed_video.fields  import  EmbedVideoField
from django.core.validators import RegexValidator

# from django.contrib.gis.db.models import PointField
# from django.contrib.gis.db import models
# Create your models here.

class banner(models.Model):
    image=models.ImageField(blank=False,null=False)

    def __str__(self):
        return "banner"


# numeric=RegexValidator(r'^[0-9+]','only digit characters.')
class enquire_now(models.Model):

    name = models.CharField(max_length=100, default="")
    # Last_name = models.CharField(max_length=100,default="")
    numeric=RegexValidator(r'^[0-9+]','only digit characters.')
    Mobile_number = models.CharField(validators=[numeric],max_length=10,blank=True)
    email = models.EmailField(max_length=100,default="")
    enquiry_type=models.CharField(max_length=100, blank=True)
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __str__(self):
        return self.first_name

class Introduction(models.Model):
    title=models.CharField(max_length=200,blank=False)
    text=models.TextField(max_length=600,blank=False)
    address=models.TextField(max_length=1000,blank=False)

    def __str__(self):
        return self.title

    
class brochure(models.Model):
    title=models.CharField(max_length=100,blank=False)
    content=models.TextField(max_length=100,blank=False)   
    image=models.ImageField(blank=False,null=False) 
    def __str__(self):
        return self.title

class Logo(models.Model):
    main_logo = models.ImageField(blank=False, upload_to="logo_images")
    secondary_logo = models.ImageField(blank=False, upload_to="logo_images")
    third_logo=models.ImageField(blank=False, upload_to="logo_images")

    def __str__(self):
        return "Logo"


class overview(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    # webp_image=models.ImageField(blank=False, upload_to='overview_images')
    png_image=models.ImageField(blank=False,  upload_to="overview_images")

    def __str__(self):
        return self.title
    
class configuration(models.Model):
    title=models.TextField(max_length=30,blank=False)
    text=models.TextField(max_length=30,blank=False)

    def __str__(self):
        return self.title



# class configuration1(models.Model):
#     title=models.TextField(max_length=30,blank=False)
#     text=models.TextField(max_length=30,blank=False)

#     def __str__(self):
#         return self.title


    
class gallery(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(blank=False,  upload_to="gallery_images")
    # image=models.ImageField(blank=False,  upload_to="gallery_images")

    def __str__(self):
        return self.name
    
class amenities(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(blank=False,upload_to="amenities_images")

    def __str__(self):
        return self.name
    

class walkthrough(models.Model):
    video = models.TextField(blank=False, default='https://www.youtube.com/embed/6HeE9W2bR-I')

    def __str__(self):
        return "Walkthrough"

class know_your_locality(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to="locality_images")
    discription=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class locality_map(models.Model):
    location = models.TextField(blank=False, default="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3806.012976551304!2d78.429541!3d17.459093!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd4a220dc7610156d!2sBrigade%20Citadel!5e0!3m2!1sen!2sin!4v1632476420684!5m2!1sen!2sin&rel=0")
    
    def __str__(self):
        return "locality_map"
    
class Registration(models.Model):
    discription=models.TextField(max_length=100,blank=False)

    def __str__(self):
        return "Registration"




