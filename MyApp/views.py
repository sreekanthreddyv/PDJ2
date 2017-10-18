from django.shortcuts import render
from .models import Hello
from datetime import datetime

# Create your views here.
def hacker(request):
	return render(request, 'example_1.html')

def hell(request):
	variable = Hello.objects.all()
	return render(request, 'example_2.html', {'variable': variable})

def check_filter_tag(request):
	variable = "<strong>http://www.No.com Pain, No Gain</strong>"
	now = datetime.now()
	context = {'variable': variable, 'now':now}
	return render(request, 'example_1.html', context)

def test_cycle(request):
	names = ['Sreekanth', 'Harsha', 'Hacker', 'Chinna', 'Mr. Robot']
	# time_format = [ DATE_FORMAT, DATETIME_FORMAT, SHORT_DATE_FORMAT or SHORT_DATETIME_FORMAT]
	return render(request, 'example_1.html', {'names': names})

def regrp(request):
	cities = [
	    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
	    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
	    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
	    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
	    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
	]
	return render(request, "example_3.html", {'cities': cities})
