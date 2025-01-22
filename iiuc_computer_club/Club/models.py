from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')

    def __str__(self):
        return f'{self.user.username} Profile'

class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='notices/', null=True, blank=True)
    date_posted = models.DateField(default=now)

    def __str__(self):
        return self.title

class Notification(models.Model):
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification {'Read' if self.is_read else 'Unread'}"



class Announcement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='announcements/', null=True, blank=True)
    date_posted = models.DateField(default=now)

    def __str__(self):
        return self.name

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    position = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='events_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    approved = models.BooleanField(default=False)
    feature = models.CharField(
        max_length=50,
        choices=[
            ('academic', 'Academic'),
            ('taskmanagement', 'Task Management'),
            ('suggestions', "Suggestions"),
            ('special', 'Special'),
        ],
        default='suggestions'
    )

    def _str_(self):
        return self.title