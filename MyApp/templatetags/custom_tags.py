from django import template
from ..models import Hello
from datetime import datetime

register = template.Library()

@register.simple_tag
def get_count():
	return Hello.objects.count()

@register.inclusion_tag('example_1.html')
def list_person():
	variable = Hello.objects.all()
	hell = "hacker"
	return {'variable': hell}

@register.filter(is_safe = True)
def cut(value, arg):
	return value.replace(arg, 'Yes')

@register.simple_tag
def current_time(format_string):
	now = datetime.now()
	return now.strftime(format_string)
