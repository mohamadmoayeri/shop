from django.db import models

# Create your models here.

from django.contrib.auth.models import User,AbstractUser

from django.utils.timezone import now

from django.core.exceptions import ValidationError

import re

from django.urls import reverse

from django.utils.html import mark_safe

def VALID(value):

  x=re.match('^09\d{9}$',value)

  if x :
    return value
  else:
     raise ValidationError('the phone number is incorrect')

class User(AbstractUser):

    avatar=models.ImageField(upload_to='files/avatars',null=True,blank=True)

    phone=models.CharField(max_length=11,unique=True,null=True,blank=True,validators=[VALID],help_text='example:09121112020')

    g=[('m','Male'),('f','Female'),('c','Costum'),('p','Prefer Not To Say')]

    gender=models.CharField(max_length=10,choices=g,default='m')

    birthday=models.DateField(null=True,blank=True,default=now)

    def __str__(self):
        
        return self.username
    def image_tag(self):

      if self.avatar:

         return mark_safe('<img src="%s"  onerror=this.src="/static/images/no.png"  class="rounded-circle" width="75" height="75" /><br/>'%(self.avatar.url))
    
      else:

        return mark_safe('<img src="/static/images/no.png"  width="75" height="75"><br/>')

    image_tag.short_description='avatar'



class ads(models.Model):


    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    image=models.ImageField(upload_to='files/images',null=False,blank=False)

    title=models.CharField(max_length=150,null=False,blank=False)

    price=models.SlugField(max_length=30,blank=False,null=False)

    c=[('electronics','Electronics'),('restaurants','Restaurants')]

    category=models.CharField(max_length=100,choices=c,default='electronics')

    available=models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)

    updatted_at=models.DateTimeField(auto_now=True, auto_now_add=False)


    def get_absolute_url(self):
        return reverse("delete_ads", args=[self.id])

    def __str__(self):
       return self.title
    




    

