# Generated by Django 3.2.17 on 2023-03-10 13:15

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_fullctl", "0030_alter_response_content"),
        ("prefix_meta", "0015_auto_20230308_1138"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArinAPIRequest",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("django_fullctl.request",),
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ArinWhoWasData",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("prefix_meta.data",),
        ),
        migrations.CreateModel(
            name="ArinWhoWasRequest",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("prefix_meta.request",),
        ),
        migrations.CreateModel(
            name="ArinWhoWasTask",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("django_fullctl.task",),
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="IRRExplorerData",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("prefix_meta.data",),
        ),
        migrations.CreateModel(
            name="IRRExplorerRequest",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("prefix_meta.request",),
        ),
        migrations.AddField(
            model_name="response",
            name="content",
            field=models.TextField(
                blank=True,
                help_text="raw content of response - may not be set if data and content are equal.",
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="ArinAPIRequestWhoWas",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("prefix_meta.arinapirequest",),
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
    ]
