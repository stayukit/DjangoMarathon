# Generated by Django 4.2.1 on 2023-05-15 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_staff"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Category",
            new_name="Categories",
        ),
    ]