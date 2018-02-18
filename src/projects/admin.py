from django.contrib import admin

from .models import Project, Post

# Register your models here.
class InlineImage(admin.TabularInline):
	model = Post
	fields = ['multi_images',]


class PostAdmin(admin.ModelAdmin):
    inlines = [InlineImage,]


admin.site.register(Project, PostAdmin)