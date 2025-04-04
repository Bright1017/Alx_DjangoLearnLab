from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notification_notifications_recipient")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notification_notifications_actor")
    verb = models.CharField(max_length=255)  # The action (e.g., "liked your post")

    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Content type (e.g., Post, Comment)
    target_object_id = models.PositiveIntegerField()  # Object ID
    target = GenericForeignKey('target_content_type', 'target_object_id')  # Generic relation to any model

    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Whether the notification has been read
