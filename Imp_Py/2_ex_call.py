class Multiplier:
	def __init__(self, factor):
		self.factor = factor

	def __call__(self, value):
		return value * self.factor

times2 = Multiplier(2)
print(times2(3))
