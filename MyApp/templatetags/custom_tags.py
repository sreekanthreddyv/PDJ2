from django import template
from ..models import Hello

register = template.Library()

@register.simple_tag
def get_count():
	return Hello.objects.count()

@register.inclusion_tag('example_1.html')
def list_person():
	variable = Hello.objects.all()
	hell = "hacker"
	return {'variable': hell}
