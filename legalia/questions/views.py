# Create your views here.
from django.shortcuts import render
from questions.models import Question

def index(request):
	print request.user.is_authenticated()
	context = {
		'auth': request.user.is_authenticated(),
		'user': request.user,
		'questions': Question.objects.all()[:15]
	}
	return render(request, 'questions/index.html', context)

def one(request, id):
	print request.user.is_authenticated()
	context = {
		'auth': request.user.is_authenticated(),
		'user': request.user,
		'questions': Question.objects.all()[:15]
	}
	return render(request, 'questions/index.html', context)
