from django.contrib import admin

from .models import Experience

# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
	list_display = ["title", "timestam", "updated"]
	sarch_fields = ["title", "description"]
	class Meta:
		model = Experience

admin.site.register(Experience, ExperienceAdmin)