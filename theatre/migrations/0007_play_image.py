# Generated by Django 5.0.1 on 2024-01-17 13:26

import theatre.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("theatre", "0006_performance"),
    ]

    operations = [
        migrations.AddField(
            model_name="play",
            name="image",
            field=models.ImageField(
                null=True, upload_to=theatre.models.play_image_file_path
            ),
        ),
    ]
