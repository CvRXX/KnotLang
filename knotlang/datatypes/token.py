# A datatype for tokens with representation.
class Token(object):
	def __init__(self,type,value,knotId):
		self.type = type
		self.value = value
		self.knotId = knotId

	def __str__(self):
		return 'Token({type}, {value}, {knotId})'.format(
			type=self.type,
			value=repr(self.value),
			knotId=self.knotId
			)
	def __repr__(self):
		return self.__str__()