# Generated by Django 4.0.6 on 2022-08-23 17:57

import django.db.models.deletion
from django.db import migrations, models

import Eduplatform_site.mixins


class Migration(migrations.Migration):

    dependencies = [
        ("learning", "0004_create_test_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("text", models.CharField(max_length=255)),
                ("is_important", models.BooleanField(default=False)),
                (
                    "test",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="learning.test"),
                ),
            ],
            options={
                "verbose_name": "test_question",
                "verbose_name_plural": "test_questions",
            },
            bases=(models.Model, Eduplatform_site.mixins.DateTimeMixinModel),
        ),
    ]
