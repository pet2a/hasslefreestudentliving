# Generated by Django 4.2 on 2024-12-06 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CribDashApp', '0023_remove_apartments_created_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apartments',
            new_name='Apartments1',
        ),
        migrations.RenameModel(
            old_name='Appartment',
            new_name='Appartment1',
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contact1',
        ),
        migrations.RenameModel(
            old_name='ContactInquiry',
            new_name='ContactInquiry1',
        ),
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserProfile1',
        ),
    ]
