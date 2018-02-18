from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Event

# Create your views here.
def events_list(request):
	queryset = Event.objects.all()

	context = { 
		"object_list": queryset,
	}
	return render(request, "events.html", context)