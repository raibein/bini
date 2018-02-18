from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	mobile = models.IntegerField()
	address = models.CharField(max_length=100)
	message = models.TextField()
	timestam = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("contact:detail", kwargs={"id": self.id})
