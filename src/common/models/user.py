from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from common.models.entity import Entity, EntityUserManager


class ExtendedUser(Entity, AbstractUser):
    is_doctor = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)

    objects = EntityUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
