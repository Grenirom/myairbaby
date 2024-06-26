from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


from .managers import UserManager


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True, db_index=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=100, blank=True, null=True)
    is_allowed = models.BooleanField(default=False)

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




