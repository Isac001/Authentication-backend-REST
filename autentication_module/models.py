# Django Imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 
from django.db import models

# Module Imports
from autentication_module.managers import UserManager

# User Class 
class User(AbstractBaseUser, PermissionsMixin):

    # User Fields
    user_name = models.CharField(_("Name of User"), max_length=255, null=False)
    user_email = models.CharField(_("Email of User"), max_length=255, null=False)
    user_password = models.CharField(_("Password of User"), max_length=255, null=False)
    user_cpf = models.CharField(_("CPF User"), max_length=14, null=False, unique=True)

    # Access and permission data
    is_staff = models.BooleanField(_("Admin?"), default=False)
    is_active = models.BooleanField(_("Active?"), default=True)
    is_trusty = models.BooleanField(_("Trusty?"), default=True)

    # Authentication field
    USERNAME_FIELD = "user_email"

    # Manager for create operations
    objects = UserManager()

    # Default return
    def __str__(self):

        return self.user_email

    class Meta:

        db_table = "autentication_module"
        app_label = "autentication_module"
        constraints = [
            models.UniqueConstraint(fields=['user_cpf'], name='unique_cpf'),
            models.UniqueConstraint(fields=['user_email'], name='unique_email')
        ]
