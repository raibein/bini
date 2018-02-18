from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Project, Post

# Create your views here.
def projects_list(request):
	single_image = Project.objects.all()
	multiple_image = Post.objects.all()

	context = { 
		"single_image_list": single_image,
		"multiple_image_list": multiple_image,
	}
	return render(request, "projects.html", context)



def gallery_list(request, id=None):
	single_image = Project.objects.all().filter(id=id)
	multiple_image = Post.objects.all().filter(projectId_id=id)

	context = { 
		"single_image_list": single_image,
		"multiple_image_list": multiple_image,
	}

	return render(request, "galleries.html", context)


'''
def gallery_list(request, id=None):
	#instance = Profile.objects.get(id=4)
	#instance = Profile.objects.get(id=id)
	instance = get_object_or_404(Post, id=4)
	context = {
		"title": "Detail",
		"instance": instance
	}
	return render(request, "galleries.html", context)
'''

