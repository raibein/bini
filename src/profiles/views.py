from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

#from .forms import ProfileForm
from .models import Profile

from .forms import ContactForm

#from contacts.models import Contact
from professional_skills.models import ProfessionalSkill
from technical_skills.models import TechnicalSkill
from experiences.models import Experience
from awards.models import Award
from events.models import Event
from qualifications.models import Qualification
from projects.models import Project

# Create your views here.
#def profile_home(request):
#	return render(request, "base.html", {})

def profile_list(request):
	queryset = Profile.objects.all()
	queryset1 = ProfessionalSkill.objects.all()[:4]
	queryset2 = TechnicalSkill.objects.all()[:4]
	queryset3 = Experience.objects.all()[:4]
	queryset4 = Award.objects.all()[:4]
	queryset5 = Event.objects.all()[:4]
	queryset6 = Qualification.objects.all()
	form = ContactForm(request.POST or None)
	project = Project.objects.all()[:4]

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully posted your message")
		#return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Could not send your message")

	context = {
		"object_list": queryset,
		"profess_list": queryset1,
		"techns_list": queryset2,
		"exper_list": queryset3,
		"award_list": queryset4,
		"event_list": queryset5,
		"ql_list": queryset6,
		"form": form,
		"project_list": project,
	}
	return render(request, "base.html", context)




def profile_detail(request, id=None):
	#instance = Profile.objects.get(id=1)
	instance = get_object_or_404(Profile, id=1)
	context = {
		"title": "Detail",
		"instance": instance
	}
	return render(request, "detail.html", context)






def profile_create(request):
	form = ProfileForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully posted your message")
		#return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Could not send your message")

	context = {
		"form": form,
	}

	return render(request, "profile_form.html", context)
	










def profile_update(request):
	return HttpResponse("<h1> Update </h1>")

def profile_delete(request):
	return HttpResponse("<h1> Delete </h1>")


