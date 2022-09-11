# Generated by Django 4.0.6 on 2022-08-23 17:58

import django.db.models.deletion
from django.db import migrations, models

import Eduplatform_site.mixins


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_create_group_model"),
        ("learning", "0006_create_answer_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.PositiveSmallIntegerField(default=0)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.student",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="learning.test"),
                ),
            ],
            options={
                "verbose_name": "test_attempt",
                "verbose_name_plural": "test_attempts",
            },
            bases=(models.Model, Eduplatform_site.mixins.DateTimeMixinModel),
        ),
    ]
