# Generated by Django 5.0.7 on 2024-07-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rtech", "0002_launches"),
    ]

    operations = [
        migrations.AlterField(
            model_name="launches",
            name="rocket",
            field=models.CharField(default="Default Rocket Name", max_length=100),
        ),
        migrations.AlterField(
            model_name="launches",
            name="youtube",
            field=models.URLField(),
        ),
    ]
