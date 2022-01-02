from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    branch =models.CharField(max_length=30,null=True)
    role =models.CharField(max_length=15,null=True)

    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username



class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate =models.CharField(max_length=30,null=True)
    branch =models.CharField(max_length=30)
    subject =models.CharField(max_length=30)
    notesfile =models.FileField(null=True)
    filetype =models.CharField(max_length=30)
    description =models.CharField(max_length=200,null=True)
    year =models.CharField(max_length=30,null=True)
    notestype=models.CharField(max_length=30,null=True)
    status =models.CharField(max_length=30)

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email
    

    