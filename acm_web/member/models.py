from django.db import models

# Create your models here.

# The Member class will model the 
# normal data of a member of the group

class Member(models.Model):
    fName = models.CharField(max_length=25)
    lName = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    pic   = models.ImageField(upload_to='member/pic')
    email = models.EmailField(max_length=254)
    admin = models.BooleanField()
    member= models.BooleanField()
    links = models.TextField()
    bio   = models.TextField()

    
