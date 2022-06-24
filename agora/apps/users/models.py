from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """A model manager for the custom User with no username field.

    The default create_superuser method takes a username position no matter if
    the field is set to None on the custom model. We must create a custom
    UserManager that does not take username as a argument in order to create
    a superuser sans username.
    """

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """A custom user model easier to modify than the Django default."""

    # usernames are not needed on this site so the field is set to None
    username = None

    # the field is unique otherwise USERNAME_FIELD cannot point to email
    email = models.EmailField('email address', unique=True)

    # use the model's email field as the unique identifier
    USERNAME_FIELD = 'email'
    # set to an empty list so that USERNAME_FIELD is not included by default
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __repr__(self):
        return f'<User(email={self.email})>'

    def __str__(self):
        return f'{self.email}'
