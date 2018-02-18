from django import forms

from contacts.models import Contact

'''
from .models import Profile


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
			"name",
			"email",
		]
'''

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			"name",
			"email",
			"mobile",
			"address",
			"message",
		]

