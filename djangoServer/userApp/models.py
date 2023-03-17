# import required modules 

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

  
# Create a custom user manager that inherits from BaseUserManager
# BaseUserManager provides methods to create regular/super users
# it has built in password hashing, email normalisation (email in small caps)
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, mobile_number=None, address=None, account_number=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        # convert email characters to small caps
        email = self.normalize_email(email)
         
        # create a user instance
        user = self.model(email=email, password=password, username=username, mobile_number=mobile_number, address=address, account_number=account_number, **extra_fields)
        
        # hash and save password
        user.set_password(password)
        
        # save the user to database
        user.save(using=self._db)
        
        #return saved user
        return user
 
    def create_superuser(self, email, username, password, mobile_number=None, address=None, account_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # create a new user with the create_user method above
        # include extra fields for is_staff and is_superuser
        # return created user
        return self.create_user(email, username, password, mobile_number, address, account_number, **extra_fields)


# AbstractBaseUser helps create and customise an inbuilt basic user model 
# PermissionsMixin helps manage authentication and authorization 
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128, blank=False)
    mobile_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200, null=True)
    account_number = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    
    # inbuilt feature from PermissionsMixin for setting priviledges
    is_staff = models.BooleanField(default=False)

    # set the user name as a unique identifier and can be used for authentication
    USERNAME_FIELD = 'username'
    
    EMAIL_FIELD = 'email'
    
    # list required fields
    REQUIRED_FIELDS = ['email', 'password']

    # this gives access to methods defined in CustomUserManager
    objects = CustomUserManager()

    def __str__(self):
        return self.email


