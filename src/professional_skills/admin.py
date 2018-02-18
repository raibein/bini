from django.contrib import admin

from .models import ProfessionalSkill

# Register your models here.
class ProfessionalAdmin(admin.ModelAdmin):
	list_display = ["title", "percentage", "timestam", "updated"]
	sarch_fields = ["title"]
	class Meta:
		model = ProfessionalSkill

admin.site.register(ProfessionalSkill, ProfessionalAdmin)