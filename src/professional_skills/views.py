from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
#from django.shortcuts import render_to_response

from .models import ProfessionalSkill

from technical_skills.models import TechnicalSkill

# Create your views here.
def pro_list(request):
	queryset = ProfessionalSkill.objects.all()
	techSkill = TechnicalSkill.objects.all()

	context = { 
		"prof_list": queryset,
		"techn_list": techSkill,
	}
	return render(request, "pro.html", context)
	#entries = abouts.objects.all()[:4]
	#return render_to_response('about.html', {'abouts': entries})









def pro_detail(request, id=None):
	return HttpResponse("<h1> Detail </h1>")

def pro_create(request):
	return HttpResponse("<h1> Create </h1>")

def pro_update(request):
	return HttpResponse("<h1> Update </h1>")

def pro_delete(request):
	return HttpResponse("<h1> Delete </h1>")