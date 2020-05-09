from typing import List
from knotlang.datatypes.token import *

# A datatype for state.
class State(object):
	def __init__(self, tokens, pc, memory, pointer, input, output):
		self.tokens = tokens # The full list of tokens (needed for jumping)
		self.pc = pc # The current token to be run
		self.memory=memory # The memory buffer of the program
		self.pointer=pointer # The current byte pointed at in the memory
		self.input=input # The input buffer
		self.output=output # The output buffer

# Returns a state initialized for a starting program.
# init::[token]->int->[int]->state
def init(tokens: List[Token], ramsize: int, input: List[int]):
	return State(tokens, 0, [0]*ramsize,0,input,[])
		