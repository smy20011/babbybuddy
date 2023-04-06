# Generated by Django 2.2.1 on 2019-06-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("babybuddy", "0006_auto_20190502_1744"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("fr", "French"),
                    ("de", "German"),
                    ("sv", "Swedish"),
                ],
                default="en",
                max_length=255,
                verbose_name="Language",
            ),
        ),
    ]