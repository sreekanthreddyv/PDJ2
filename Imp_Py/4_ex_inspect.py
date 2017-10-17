import inspect

def complex_function(a, b, c=True, d=False, *e, **f):
	pass

# get all details about arguments passed
print(inspect.getargspec(complex_function))

# get Info about default values
def get_defaults(func):
	args, varargs, varkwargs, defaults = inspect.getargspec(func)
	index = len(args) - len(defaults) # Index of the first optional argument
	return dict(zip(args[index:], defaults))

print(get_defaults(complex_function))
