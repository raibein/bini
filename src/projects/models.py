from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=100)
	desciption = models.TextField()
	album_photo = models.ImageField(height_field="album_height_image", width_field="album_width_image")
	album_height_image = models.IntegerField(default=0)
	album_width_image = models.IntegerField(default=0)
	timestam = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("projects:galleries", kwargs={"id": self.id})
		#return "/profiles/%s/" %(self.id)


	
class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	multi_images = models.ImageField(blank=True, null=True, height_field="multi_height_image", width_field="multi_width_image")
	multi_height_image = models.IntegerField(default=0)
	multi_width_image = models.IntegerField(default=0)
	projectId = models.ForeignKey(Project)
	


