from django.contrib import admin

from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ["name", "dob", "email", "gender"]
	search_fields=["name", "email"]
	class Meta:
		model = Profile


admin.site.register(Profile, ProfileAdmin)