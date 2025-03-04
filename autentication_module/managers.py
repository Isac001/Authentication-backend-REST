# Django imports
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    def get_by_natural_key(self, user_email):
        return self.get(user_email=user_email)

    def create_user(self, user_email, password, **extra_fields):

        if not user_email:

            raise ValueError(_("The email must be set"))

        email = self.normalize_email(user_email)
        user = self.model(user_email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, user_email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_trusty", True)

        if extra_fields.get('is_staff') is not True:

            raise ValueError(_("Superuser must be have is_staff=True"))

        if extra_fields.get('is_superuser') is not True:

            raise ValueError(_("Superuser must have is_superuser=True"))

        return self.create_user(user_email, password, **extra_fields)