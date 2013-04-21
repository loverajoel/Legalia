# Create your views here.
from django.shortcuts import render

def index(request):
	print request.user.is_authenticated()
	context = {'auth': request.user.is_authenticated(), 'user': request.user}
	return render(request, 'questions/index.html', context)
