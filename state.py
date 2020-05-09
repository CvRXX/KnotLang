class State(object):
	"""docstring for state"""
	def __init__(self, tokens, pc, memory, pointer, input, output):
		self.tokens = tokens
		self.pc = pc
		self.memory=memory
		self.pointer=pointer
		self.input=input
		self.output=output

def init(tokens, ramsize, input):
	return State(tokens, 0, [0]*ramsize,0,input,[])
		