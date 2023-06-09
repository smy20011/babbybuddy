# Generated by Django 2.2 on 2019-04-17 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_child_picture"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="child",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["last_name", "first_name"],
                "verbose_name": "Child",
                "verbose_name_plural": "Children",
            },
        ),
        migrations.AlterModelOptions(
            name="diaperchange",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["-time"],
                "verbose_name": "Diaper Change",
                "verbose_name_plural": "Diaper Changes",
            },
        ),
        migrations.AlterModelOptions(
            name="feeding",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["-start"],
                "verbose_name": "Feeding",
                "verbose_name_plural": "Feedings",
            },
        ),
        migrations.AlterModelOptions(
            name="note",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["-time"],
                "verbose_name": "Note",
                "verbose_name_plural": "Notes",
            },
        ),
        migrations.AlterModelOptions(
            name="sleep",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["-start"],
                "verbose_name": "Sleep",
                "verbose_name_plural": "Sleep",
            },
        ),
        migrations.AlterModelOptions(
            name="timer",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["-active", "-start", "-end"],
                "verbose_name": "Timer",
                "verbose_name_plural": "Timers",
            },
        ),
        migrations.AlterModelOptions(
            name="tummytime",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["-start"],
                "verbose_name": "Tummy Time",
                "verbose_name_plural": "Tummy Time",
            },
        ),
        migrations.AlterModelOptions(
            name="weight",
            options={
                "default_permissions": ("view", "add", "change", "delete"),
                "ordering": ["-date"],
                "verbose_name": "Weight",
                "verbose_name_plural": "Weight",
            },
        ),
        migrations.AlterField(
            model_name="child",
            name="birth_date",
            field=models.DateField(verbose_name="Birth date"),
        ),
        migrations.AlterField(
            model_name="child",
            name="first_name",
            field=models.CharField(max_length=255, verbose_name="First name"),
        ),
        migrations.AlterField(
            model_name="child",
            name="last_name",
            field=models.CharField(max_length=255, verbose_name="Last name"),
        ),
        migrations.AlterField(
            model_name="child",
            name="picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="child/picture/",
                verbose_name="Picture",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="slug",
            field=models.SlugField(
                editable=False, max_length=100, unique=True, verbose_name="Slug"
            ),
        ),
        migrations.AlterField(
            model_name="diaperchange",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="diaper_change",
                to="core.Child",
                verbose_name="Child",
            ),
        ),
        migrations.AlterField(
            model_name="diaperchange",
            name="color",
            field=models.CharField(
                blank=True,
                choices=[
                    ("black", "Black"),
                    ("brown", "Brown"),
                    ("green", "Green"),
                    ("yellow", "Yellow"),
                ],
                max_length=255,
                verbose_name="Color",
            ),
        ),
        migrations.AlterField(
            model_name="diaperchange",
            name="solid",
            field=models.BooleanField(verbose_name="Solid"),
        ),
        migrations.AlterField(
            model_name="diaperchange",
            name="time",
            field=models.DateTimeField(verbose_name="Time"),
        ),
        migrations.AlterField(
            model_name="diaperchange",
            name="wet",
            field=models.BooleanField(verbose_name="Wet"),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="amount",
            field=models.FloatField(blank=True, null=True, verbose_name="Amount"),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="feeding",
                to="core.Child",
                verbose_name="Child",
            ),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="duration",
            field=models.DurationField(
                editable=False, null=True, verbose_name="Duration"
            ),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="end",
            field=models.DateTimeField(verbose_name="End time"),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="method",
            field=models.CharField(
                choices=[
                    ("bottle", "Bottle"),
                    ("left breast", "Left breast"),
                    ("right breast", "Right breast"),
                ],
                max_length=255,
                verbose_name="Method",
            ),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="start",
            field=models.DateTimeField(verbose_name="Start time"),
        ),
        migrations.AlterField(
            model_name="feeding",
            name="type",
            field=models.CharField(
                choices=[("breast milk", "Breast milk"), ("formula", "Formula")],
                max_length=255,
                verbose_name="Type",
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="note",
                to="core.Child",
                verbose_name="Child",
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="note",
            field=models.TextField(verbose_name="Note"),
        ),
        migrations.AlterField(
            model_name="note",
            name="time",
            field=models.DateTimeField(auto_now=True, verbose_name="Time"),
        ),
        migrations.AlterField(
            model_name="sleep",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sleep",
                to="core.Child",
                verbose_name="Child",
            ),
        ),
        migrations.AlterField(
            model_name="sleep",
            name="duration",
            field=models.DurationField(
                editable=False, null=True, verbose_name="Duration"
            ),
        ),
        migrations.AlterField(
            model_name="sleep",
            name="end",
            field=models.DateTimeField(verbose_name="End time"),
        ),
        migrations.AlterField(
            model_name="sleep",
            name="start",
            field=models.DateTimeField(verbose_name="Start time"),
        ),
        migrations.AlterField(
            model_name="timer",
            name="active",
            field=models.BooleanField(
                default=True, editable=False, verbose_name="Active"
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="duration",
            field=models.DurationField(
                editable=False, null=True, verbose_name="Duration"
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="end",
            field=models.DateTimeField(
                blank=True, editable=False, null=True, verbose_name="End time"
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="name",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Name"
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="start",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Start time"
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="timers",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="tummytime",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tummy_time",
                to="core.Child",
                verbose_name="Child",
            ),
        ),
        migrations.AlterField(
            model_name="tummytime",
            name="duration",
            field=models.DurationField(
                editable=False, null=True, verbose_name="Duration"
            ),
        ),
        migrations.AlterField(
            model_name="tummytime",
            name="end",
            field=models.DateTimeField(verbose_name="End time"),
        ),
        migrations.AlterField(
            model_name="tummytime",
            name="milestone",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Milestone"
            ),
        ),
        migrations.AlterField(
            model_name="tummytime",
            name="start",
            field=models.DateTimeField(verbose_name="Start time"),
        ),
        migrations.AlterField(
            model_name="weight",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="weight",
                to="core.Child",
                verbose_name="Child",
            ),
        ),
        migrations.AlterField(
            model_name="weight",
            name="date",
            field=models.DateField(verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="weight",
            name="weight",
            field=models.FloatField(verbose_name="Weight"),
        ),
    ]
