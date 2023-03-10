# Generated by Django 4.1.7 on 2023-03-13 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coder",
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
                ("name", models.CharField(max_length=255)),
                ("hourly_rate", models.IntegerField()),
                ("commit_hours", models.IntegerField()),
                ("hired", models.IntegerField(default=0)),
                ("skill_set", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("video_intro", models.CharField(max_length=255)),
                ("work_history", models.TextField()),
                ("github_link", models.CharField(max_length=255)),
                ("linkedin_link", models.CharField(max_length=255)),
                ("portfolio_link", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("is_featured", models.BooleanField(default=False)),
                ("photo", models.ImageField(upload_to="media/coders/%Y/%m/")),
                ("created_date", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
