from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ColorfulHairCount(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='colorful_hair_counts')
        timestamp = models.DateTimeField(default=timezone.now)
        value = models.IntegerField(default=1)

        def __str__(self):
            return f"{self.user.username} counted {self.value} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

        class Meta:
            ordering = ['-timestamp']
