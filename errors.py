class Error(object):
	def __init__(self,type,value,knotId):
		self.type = type
		self.value = value
		self.knotId = knotId

	def __str__(self):
		return 'An error has occured at knot: {knotId}\n{type}: {value}'.format(
			knotId=self.knotId,
			type=self.type,
			value=repr(self.value)
			)
	def __repr__(self):
		return self.__str__()
def mergeErrors(result):
	errors = list(filter(lambda x: not x.succeeded, result))
	if len(errors):
		return errors[0]
	else:
		return succes(list(map(lambda x: x.value, result)))
class UnknownToken(Error):
	def __init__(self,value,knotId):
		super().__init__("Unknown Token error", value, knotId)

class UnexpectedToken(Error):
	def __init__(self,value,knotId):
		super().__init__("Unexpected Token error", value, knotId)
class UnexpectedEndOfFile(Error):
	def __init__(self,value,knotId):
		super().__init__("The file has ended Unexpectedtly", value, knotId)

class MemoryOverflow(Error):
	def __init__(self,value,knotId):
		super().__init__("Memoryoverflow, the requested pointer address is outside of the memory range", value, knotId)

class MemoryUnderflow(Error):
	def __init__(self,value,knotId):
		super().__init__("Memoryunderflow, the requested pointer address is outside of the memory range", value, knotId)

class InputEmpty(Error):
	def __init__(self,knotId):
		super().__init__("The input buffer is accessed but empty", None, knotId)

class JumpOverflow(Error):
	def __init__(self,value,knotId):
		super().__init__("The jumpvalue is highter than the lenght of the program", value, knotId)

class JumpUnderflow(Error):
	def __init__(self,value,knotId):
		super().__init__("The jumpvalue is lower than 1", value, knotId)

class expected(object):
	def __init__(self,succeeded,value):
		self.succeeded = succeeded
		self.value = value
def succes(value):
	return expected(True, value)
def failed(value):
	return expected(False, value)