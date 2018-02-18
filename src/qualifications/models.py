from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class Qualification(models.Model):
	university = models.CharField(max_length=120)
	degree = models.CharField(max_length=120)
	division = models.CharField(max_length=10, blank=True)
	timestam = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return (self.university)

	def get_absolute_url(self):
		return reverse("ql:detail", kwarg={"id":self.id})
