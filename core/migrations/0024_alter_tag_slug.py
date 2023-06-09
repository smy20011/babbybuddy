# Generated by Django 4.1.2 on 2022-10-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0023_alter_tag_options_alter_bmi_tags_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(
                allow_unicode=True, max_length=100, unique=True, verbose_name="slug"
            ),
        ),
    ]
