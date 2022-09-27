# Generated by Django 4.1 on 2022-09-24 20:20

import Eduplatform_site.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'unique_together': {('photo',)},
            },
            bases=(models.Model, Eduplatform_site.mixins.DateTimeMixinModel),
        ),
    ]