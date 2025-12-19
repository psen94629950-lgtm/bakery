from django.db import models


# Create your models here.
class Contactform (models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200) 
    subject=models.CharField(max_length=200)
    message=models.TextField()


# our about model 
class About_d(models.Model):
    About_d_title=models.CharField(max_length=200)
    About_d_description=models.TextField()
    feature_1 = models.CharField(max_length=100, blank=True, null=True)
    feature_2 = models.CharField(max_length=100, blank=True, null=True)
    feature_3 = models.CharField(max_length=100, blank=True, null=True)
    feature_4 = models.CharField(max_length=100, blank=True, null=True)
    About_d_img1=models.FileField(upload_to='About',max_length=250, null=True, default=None)
    About_d_img2=models.FileField(upload_to='About',max_length=250, null=True, default=None)


# bakery product model 
class Product_d(models.Model):
    Product_d_price=models.CharField(max_length=200)
    Product_d_name=models.CharField(max_length=200)
    Product_d_img=models.FileField(upload_to='Product',max_length=250, null=True, default=None)
    Product_d_description=models.TextField()

# our team model
class Team_d(models.Model):
    Team_d_img=models.FileField(upload_to='Team',max_length=250, null=True, default=None)
    Team_d_name=models.CharField(max_length=200)
    Team_d_position=models.CharField(max_length=200)

# client review model
class Review_d(models.Model):
    Review_d_img=models.FileField(upload_to='Review',max_length=250, null=True, default=None)
    Review_d_name=models.CharField(max_length=200)
    Review_d_position=models.CharField(max_length=200)
    Review_d_message=models.TextField()    