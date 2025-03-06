# Importing the base user manager class from Django's authentication system.
# This is used to create and manage user objects.
from django.contrib.auth.base_user import BaseUserManager

# Importing translation utility for internationalization.
from django.utils.translation import gettext_lazy as _

# Defining a custom user manager class that extends Django's BaseUserManager.
class UserManager(BaseUserManager):

    # Method to create a regular user.
    def create_user(self, user_email, password, **extra_fields):
        
        # Checking if an email is provided. If not, raise a ValueError.
        if not user_email:
            raise ValueError(_("The email must be set"))

        # Normalizing the email (converting domain part to lowercase).
        email = self.normalize_email(user_email)

        # Creating a new user instance with the provided email and additional fields.
        user = self.model(user_email=email, **extra_fields)

        # Hashing and setting the user's password.
        user.set_password(password)

        # Saving the user instance to the database.
        user.save(using=self._db)

        # Returning the created user object.
        return user
    
    # Method to create a superuser (admin user with all permissions).
    def create_superuser(self, user_email, password, **extra_fields):

        # Setting default values for necessary superuser fields.
        extra_fields.setdefault("is_staff", True)  
        extra_fields.setdefault("is_superuser", True)  
        extra_fields.setdefault("is_active", True)  
        extra_fields.setdefault("is_trusty", True)  

        # Checking if 'is_staff' is set to True, otherwise raising an error.
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True"))

        # Checking if 'is_superuser' is set to True, otherwise raising an error.
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        # Calling the create_user method to create the superuser with the provided credentials.
        return self.create_user(user_email, password, **extra_fields)
