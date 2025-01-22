from django.contrib import admin
from .models import Profile
from .models import Notice
from .models import Announcement
from .models import Event
from .models import ContactMessage,BlogPost

admin.site.register(Notice)
admin.site.register(Profile)
admin.site.register(Announcement)
admin.site.register(Event)
admin.site.register(BlogPost)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

