# Generated by Django 4.1.2 on 2023-05-06 04:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transaction", "0005_loan_total_due_loan_total_paid"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="installment_paid",
            field=models.IntegerField(default=0),
        ),
    ]