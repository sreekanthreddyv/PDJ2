class CaseInsensitive:
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			self[key.lower()] = value

	def __contains__(self, key):
		return super(CaseInsensitive, self).__contains__(key.lower())

	def __getitem__(self, key):
		return super(CaseInsensitive, self).__getitem__(key.lower())

	def __setitem__(self, key, value):
		super(CaseInsensitive, self).__setitem__(key.lower(), value)

d = CaseInsensitive(SpAm = 'eggs')

#print('spam' in d)
