# Generated by Django 5.1.3 on 2024-12-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0003_contato_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture/%Y/%m/'),
        ),
    ]
