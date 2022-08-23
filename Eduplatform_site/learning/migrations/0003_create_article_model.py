# Generated by Django 4.0.6 on 2022-08-23 16:46

import account.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_create_group_model'),
        ('learning', '0002_create_topic_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.teacher')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learning.topic')),
            ],
            options={
                'verbose_name': 'topic_articles',
                'verbose_name_plural': 'topic_articles',
            },
            bases=(models.Model, account.mixins.DateTimeMixinModel),
        ),
    ]
