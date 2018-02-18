from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Award

# Create your views here.
def awards_list(request):
	queryset = Award.objects.all()

	context = { 
		"object_list": queryset,
	}
	return render(request, "awards.html", context)