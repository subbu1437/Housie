from django.db import models
from django.utils import  timezone
import uuid


class   BaseModel(models.Model):
    created_on = models.DateTimeField('created on', default=timezone.now)
    modified_on = models.DateTimeField('modified on', default=timezone.now)
    is_deleted = models.BooleanField('Is deleted', default=False)
    is_active = models.BooleanField(default=True)
    gu_id = models.UUIDField(default=uuid.uuid4, unique=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.modified_on = timezone.now()
        super(BaseModel, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        abstract = True
