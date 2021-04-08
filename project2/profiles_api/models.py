from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
class UserProfileManager(BaseUserManager):
    """"class required by django for managing our users from management command"""

    def create_user(self, email, name, password):
        if not email:
            raise ValueError("Users Must Have EMail Address")

        # create anew user object
        user = self.model(
            email=self.normalize_email(email),
            name=self.name,
        )
        # create new pass
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """"create and save new superuser with given details"""
        """"override on create fun"""
        user = self.create_user(email, name, password)

        # make this user an admin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class USerProfile(AbstractBaseUser, PermissionsMixin):
    """a user profile in our system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        self.name

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        self.name

    def __str__(self):
        """What to show when we output an object as a string."""

        return self.email
