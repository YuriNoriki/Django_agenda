# Generated by Django 5.1.3 on 2024-12-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_contato_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture/%Y%m/'),
        ),
    ]