from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Experience

# Create your views here.
def exp_list(request):
	queryset = Experience.objects.all()

	context = { 
		"object_list": queryset,
	}
	return render(request, "experience.html", context)