class MetaClass(type):
	def __init__(cls, name, bases, attrs):
		print("Defining: {}".format(cls))
		print("Name: {}:".format(name))
		print("Bases: {}".format(bases))
		print("Attributes:")
		for (name, value) in attrs.items():
			print("\t{}: {}".format(name, value))


class RealClass(object, metaclass=MetaClass):
	spam = 'eggs'
