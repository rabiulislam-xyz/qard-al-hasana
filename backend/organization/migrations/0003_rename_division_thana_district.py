# Generated by Django 4.1.2 on 2023-03-22 10:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0002_team"),
    ]

    operations = [
        migrations.RenameField(
            model_name="thana",
            old_name="division",
            new_name="district",
        ),
    ]
