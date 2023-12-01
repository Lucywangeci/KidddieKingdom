from django.contrib import admin
from .models import ContactMessage, Hero, AboutSection, Event, Blog, TeamMember, Testimonial

# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(Hero)
admin.site.register(AboutSection)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
