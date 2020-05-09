from knotlang import operations
from knotlang.errors import succes, failed
from knotlang.datatypes.state import *
from typing import Callable
from knotlang.errors import expected

# Runs a program and returns the finalState
# getOutput::State->Callable[[State,State]]->expected{State,error}
def getOutput(state: State, loggingFunc: Callable[[State,State],None]) -> expected:
	if state.pc==len(state.tokens):
		return succes(state)

	if state.tokens[state.pc].type=="+":
		function= operations.plus

	if state.tokens[state.pc].type=="-":
		function= operations.min

	if state.tokens[state.pc].type=="output":
		function= operations.output

	if state.tokens[state.pc].type=="p+":
		function= operations.pointerPlus

	if state.tokens[state.pc].type=="p-":
		function= operations.pointerMin

	if state.tokens[state.pc].type=="input":
		function= operations.input

	if state.tokens[state.pc].type=="jumpeq":
		function= operations.jump

	result = function(state)
	if result.succeeded:
		# I know this part is not functional but I ran out of time here {
		if loggingFunc: 
			for line in loggingFunc(state, result.value):
				print(line)
		#}
		return getOutput(result.value, loggingFunc)
	else:
		return result