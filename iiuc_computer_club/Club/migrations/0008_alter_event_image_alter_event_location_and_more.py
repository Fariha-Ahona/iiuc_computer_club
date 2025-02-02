# Generated by Django 5.1.4 on 2024-12-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0007_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events_images/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
