from common.models.entity import Entity
from django.utils.translation import gettext_lazy as _
from django.db import models


class Diagnosis(Entity):
    name = models.CharField(max_length=512)
    user = models.ForeignKey(
        to='common.ExtendedUser',
        on_delete=models.DO_NOTHING,
        related_name='diagnoses',
    )

    class Meta:
        verbose_name = _('Diagnosis')
        verbose_name_plural = _('Diagnoses')

    def __str__(self):
        return self.name
