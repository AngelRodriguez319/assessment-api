"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Process(Model):

    n = models.IntegerField(
        default=0)
    k = models.IntegerField(
        default=0)
    result = models.IntegerField(
        default=0)

    user = models.ForeignKey(
        'models.User', related_name='processes',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_process'
        app_label = 'models'