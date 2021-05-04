from django.db import models
from .managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name=_('Email'),
        max_length=150,
        unique=True,
        help_text=_('User email'),
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=100,
        blank=True,
        help_text=_('User first name'),
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=100,
        blank=True,
        help_text=_('User last name'),
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined',
        auto_now_add=True,
        help_text=_('Create date of user'),
    )
    is_active = models.BooleanField(
        verbose_name=_('Is user active?'),
        default=False,
        help_text=_('Is user active?'),
    )
    is_admin = models.BooleanField(
        verbose_name='Is user admin?',
        default=False,
        help_text=_('Is user admin?'),
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
