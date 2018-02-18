from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


from .forms import ContactForm

# Create your views here.
def contact_list(request):	
	form = ContactForm(request.POST or None)

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

	return render(request, "contact.html", context)