from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

class FollowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content_type = models.ForeignKey(
                            ContentType,
                            related_name='followed_record_contenttype'
                        )
    object_id = models.PositiveIntegerField(db_index=True)
