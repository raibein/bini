from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class Profile(models.Model):
	image = models.ImageField(null=True, blank=True, width_field="width_image", height_field="height_image")
	height_image = models.IntegerField(default=0)
	width_image = models.IntegerField(default=0)
	personal_quote = models.TextField()
	name = models.CharField(max_length=30)
	dob = models.DateTimeField()
	email = models.CharField(max_length=50)
	maritialStatus = models.CharField(max_length=10)
	citizenship = models.CharField(max_length=10)
	gender = models.CharField(max_length=8)
	mobile = models.CharField(max_length=15)
	address = models.CharField(max_length=120)
	timestam = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("profiles:detail", kwargs={"id": self.id})
		#return "/profiles/%s/" %(self.id)
