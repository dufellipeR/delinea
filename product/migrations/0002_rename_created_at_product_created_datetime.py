# Generated by Django 4.0.1 on 2022-01-10 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_at',
            new_name='created_datetime',
        ),
    ]