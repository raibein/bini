from django.contrib import admin

from .models import TechnicalSkill

# Register your models here.
class TechnicalAdmin(admin.ModelAdmin):
	list_display = ["title", "percentage", "timestam", "updated"]
	sarch_fields = ["title"]
	class Meta:
		model = TechnicalSkill

admin.site.register(TechnicalSkill, TechnicalAdmin)
