# Create your views here.
from django.shortcuts import render
from questions.models import Question

def index(request):
	context = {
		'auth': request.user.is_authenticated(),
		'user': request.user,
		'questions': Question.objects.all()[:15]
	}
	return render(request, 'questions/index.html', context)

def question(request, question_id):
	context = {
		'auth': request.user.is_authenticated(),
		'user': request.user,
		'question': Question.objects.filter(id=question_id).get()
	}
	return render(request, 'questions/view.html', context)
