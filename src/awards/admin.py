from django.contrib import admin

from .models import Award

# Register your models here.
class AwardAdmin(admin.ModelAdmin):
	list_display = ["title", "timestam", "updated"]
	sarch_fields = ["title", "description"]
	class Meta:
		model = Award

admin.site.register(Award, AwardAdmin)
