# Generated by Django 5.1.4 on 2024-12-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0006_announcement_delete_annoucement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
