# Generated by Django 2.2 on 2019-05-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("babybuddy", "0004_settings_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("fr", "French")],
                default="en",
                max_length=255,
                verbose_name="Language",
            ),
        ),
    ]
