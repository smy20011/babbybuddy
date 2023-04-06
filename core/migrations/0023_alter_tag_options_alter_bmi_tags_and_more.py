# Generated by Django 4.0.3 on 2022-04-16 21:56

import core.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0022_alter_default_date_and_time"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Tag", "verbose_name_plural": "Tags"},
        ),
        migrations.AlterField(
            model_name="bmi",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="diaperchange",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="headcircumference",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="height",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="sleep",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="tummytime",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="weight",
            name="tags",
            field=core.models.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.Tagged",
                to="core.Tag",
                verbose_name="Tags",
            ),
        ),
    ]