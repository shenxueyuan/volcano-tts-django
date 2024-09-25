from django.db import migrations
from django.conf import settings


def add_default_speakers(apps, schema_editor):
    VoiceModel = apps.get_model('voice_app', 'VoiceModel')
    for speaker_id, name in settings.DEFAULT_SPEAKERS:
        VoiceModel.objects.get_or_create(
            speaker_id=speaker_id,
            defaults={
                'name': name,
                'status': 'AV'  # 'AV' 表示可用状态
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        # 替换为前一个迁移的名称
        ('voice_app', '0002_voicemodel_name_alter_voicemodel_speaker_id_and_more'),
    ]

    operations = [
        migrations.RunPython(add_default_speakers),
    ]
