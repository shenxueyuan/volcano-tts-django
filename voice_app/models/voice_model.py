from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class VoiceModel(models.Model):
    class TrainingStatus(models.TextChoices):
        TRAINING = 'TR', _('训练中')
        AVAILABLE = 'AV', _('可用')
        FAILED = 'FA', _('失败')

    speaker_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)  # 新增字段
    update_at = models.DateTimeField(auto_now=True)  # 修改为 auto_now
    status = models.CharField(
        max_length=2,
        choices=TrainingStatus.choices,
        default=TrainingStatus.AVAILABLE,  # 修改默认值
    )

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
