import uuid
from django.db import models
from django.db.models import BigAutoField
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    id = BigAutoField(primary_key=True, )
    created = models.DateTimeField(verbose_name=_("Created At"),null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    class Meta:
        abstract = True
        default_permissions = {}
        ordering = ['created']