from django.shortcuts import render
from .models import Hello

# Create your views here.
def hacker(request):
	return render(request, 'example_1.html')

def hell(request):
	variable = Hello.objects.all()
	return render(request, 'example_2.html', {'variable': variable})
