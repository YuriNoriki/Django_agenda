# Generated by Django 5.1.3 on 2025-01-10 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0007_contato_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='create_date',
            new_name='created_date',
        ),
    ]