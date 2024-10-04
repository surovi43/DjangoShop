# Generated by Django 5.1.1 on 2024-10-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                default="user_placeholder.png",
                null=True,
                upload_to="profiles",
            ),
        ),
    ]
