# Generated by Django 5.1.5 on 2025-02-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0002_alter_items_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, upload_to='Items/'),
        ),
    ]
