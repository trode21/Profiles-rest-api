from django.db import models
from django.contrib.auth.models import AbstractBaseUser #
from django.contrib.auth.models import PermissionsMixin #
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManger(BaseUserManager):
    """Manager for user Profile"""

    def create_user(self,email,name,password=None):
        """Create a new user Profile"""
        if not email:
            raise ValueError("User must have a email adress") #if this mathod is called email cannot be null

        email = self.normalize_email(email) #making the email not case senstive
        user = self.model(email = email, name=name)

        user.set_password(password) #have to do this to make sure that the password is enc
        user.save(using=self._db) #standard for saving

        return user


    def create_superuser(self,email,name,password):
        """create new superuser with given detials"""
        user = self.create_user(email, name, password)

        user.is_superuser = True #is already part of PermissionsMixin
        user.is_staff = True
        user.save(using = self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Data model for users in the system""" #doc string to tell what the class is about help reminds you
    email = models.EmailField(max_length=225, unique=True)#creating a db colomn that is named email max 225 char and cant have same email
    name = models.CharField(max_length = 225)
    is_active = models.BooleanField(default=True)# field that if a user profile is active and also allows to deactive account
    is_staff = models.BooleanField(default=False)# is staff or not


    objects = UserProfileManger()  #class not created yet

    USERNAME_FIELD = 'email' #user putting a email in, and logging in with it instead of a user name
    REQUIRED_FIELDS = ['name']

    def get_full_name(self): #self is becuse is it default with python, with a method inside a class
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return the string represtation of the user"""
        return self.email
