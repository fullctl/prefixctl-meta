# Generated by Django 3.2.15 on 2023-02-22 16:29

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prefix_meta", "0006_alter_data_date"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="data",
            unique_together=set(),
        ),
        migrations.AddIndex(
            model_name="data",
            index=models.Index(
                django.db.models.expressions.F("prefix"), name="prefix_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="data",
            index=models.Index(
                django.db.models.expressions.F("source_name"), name="source_name_idx"
            ),
        ),
    ]