# Generated by Django 3.2.10 on 2021-12-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_alter_sleep_napping"),
    ]

    operations = [
        migrations.AlterField(
            model_name="child",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Last name"
            ),
        ),
    ]
