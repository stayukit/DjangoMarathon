# Generated by Django 4.2.1 on 2023-05-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_customerform_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerform",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="customerform",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
