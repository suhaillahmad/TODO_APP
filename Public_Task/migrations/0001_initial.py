# Generated by Django 4.1.7 on 2023-02-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("task", models.CharField(blank=True, max_length=200, null=True)),
                ("is_completed", models.BooleanField(default=False)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
