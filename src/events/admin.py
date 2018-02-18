from django.contrib import admin

from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_display = ["title", "timestam", "updated"]
	sarch_fields = ["title", "description"]
	class Meta:
		model = Event

admin.site.register(Event, EventAdmin)
