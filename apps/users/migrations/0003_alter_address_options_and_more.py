# Generated by Django 5.1.1 on 2024-10-28 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_business_email_merchantapplication_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='merchantapplication',
            options={'ordering': ['-date_applied'], 'verbose_name': 'Merchant Application', 'verbose_name_plural': 'Merchant Applications'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelTable(
            name='address',
            table='addresses',
        ),
        migrations.AlterModelTable(
            name='merchantapplication',
            table='merchant_applications',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]