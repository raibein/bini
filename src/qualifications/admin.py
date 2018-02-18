from django.contrib import admin

from .models import Qualification

# Register your models here.
class QualificationAdmin(admin.ModelAdmin):
	list_display = ["university", "degree", "timestam", "updated"]
	sarch_fields = ["university", "degree"]
	class Meta:
		model = Qualification

admin.site.register(Qualification, QualificationAdmin)
