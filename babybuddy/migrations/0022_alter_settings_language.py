# Generated by Django 4.0.3 on 2022-04-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("babybuddy", "0021_alter_settings_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="language",
            field=models.CharField(
                choices=[
                    ("ca", "Catalan"),
                    ("zh-hans", "Chinese (simplified)"),
                    ("nl", "Dutch"),
                    ("en-US", "English (US)"),
                    ("en-GB", "English (UK)"),
                    ("fr", "French"),
                    ("fi", "Finnish"),
                    ("de", "German"),
                    ("it", "Italian"),
                    ("pl", "Polish"),
                    ("pt", "Portuguese"),
                    ("es", "Spanish"),
                    ("sv", "Swedish"),
                    ("tr", "Turkish"),
                ],
                default="en-US",
                max_length=255,
                verbose_name="Language",
            ),
        ),
    ]
