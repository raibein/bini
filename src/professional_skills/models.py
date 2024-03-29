from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class ProfessionalSkill(models.Model):
	title = models.CharField(max_length=50)
	percentage = models.IntegerField()
	timestam = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("pro:detail", kwargs={"id": self.id})
