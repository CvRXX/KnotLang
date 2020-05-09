from typing import List

# A union class that can be a result or error
class expected(object):
	def __init__(self,succeeded,value):
		self.succeeded = succeeded
		self.value = value

# Returns an expected that is successful.
def succes(value):
	return expected(True, value)

# Returns an expected that has failed.
def failed(value):
	return expected(False, value)

# Takes a list of expected's and checks if one has failed. If so returns the expected with the error. Otherwise returns an expected with all the values as value.
# mergeErrors::[expected]->expected
def mergeErrors(result: List[expected])->expected:
	errors = list(filter(lambda x: not x.succeeded, result))
	if len(errors):
		return errors[0]
	else:
		return succes(list(map(lambda x: x.value, result)))

# A base class for errors with representation.
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



# An error class for when an unknown token is encountered.
class UnknownToken(Error):
	def __init__(self,value,knotId):
		super().__init__("Unknown Token error", value, knotId)

# An error class for when an unexpected token is encountered.
class UnexpectedToken(Error):
	def __init__(self,value,knotId):
		super().__init__("Unexpected Token error", value, knotId)

# An error class for when an unexpected end to the file is encountered.
class UnexpectedEndOfFile(Error):
	def __init__(self,value,knotId):
		super().__init__("The file has ended Unexpectedtly", value, knotId)

# An error class for when the pointer address gets over the size of the memory.
class MemoryOverflow(Error):
	def __init__(self,value,knotId):
		super().__init__("Memoryoverflow, the requested pointer address is outside of the memory range", value, knotId)

# An error class for when the pointer address gets under zero.
class MemoryUnderflow(Error):
	def __init__(self,value,knotId):
		super().__init__("Memoryunderflow, the requested pointer address is outside of the memory range", value, knotId)

# An error class for when the inputbuffer is read but the buffer is empty.
class InputEmpty(Error):
	def __init__(self,knotId):
		super().__init__("The input buffer is accessed but empty", None, knotId)

# An error class for when a jump is attempted higher than the length of the program.
class JumpOverflow(Error):
	def __init__(self,value,knotId):
		super().__init__("The jumpvalue is highter than the lenght of the program", value, knotId)

# An error class for when a jump is attempted lower than 1.
class JumpUnderflow(Error):
	def __init__(self,value,knotId):
		super().__init__("The jumpvalue is lower than 1", value, knotId)
