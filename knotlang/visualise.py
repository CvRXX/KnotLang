from knotlang.datatypes.state import State

# Takes two states and outputs a fancy list of strings about the changes.
# visualisesStep->State->State->[str]
def visualisesStep(oldState: State, newState: State)->str:
	output = []
	output += ["=============================================="]
	output += ["Current state:"]
	if oldState.pc==len(oldState.tokens):
		output += ["	Next action: none"]
	else:
		output += ["	Next action: " + oldState.tokens[oldState.pc].type]
	output += ["	Current pointeraddress: " + str(oldState.pointer)]
	output += ["	Current value at pointer: " + str(oldState.memory[oldState.pointer])]
	if len(oldState.input):
		output += ["	Next item in input buffer: " + str(oldState.input[0])]
	else:
		output += ["	Next item in input buffer: none"]
	if len(oldState.output):
		output += ["	Last item in output buffer: " + str(oldState.output[-1])]
	else:
		output += ["	Last item in output buffer: none"]
	output += []
	output += ["After action:"]
	if oldState.pc>=len(oldState.tokens)-1:
		output += ["	Next action: none"]
	else:
		output += ["	Next action: " + newState.tokens[newState.pc].type]
	output += ["	Current pointeraddress: " + str(newState.pointer)]
	output += ["	Current value at pointer: " + str(newState.memory[newState.pointer])]
	if len(newState.input):
		output += ["	Next item in input buffer: " + str(newState.input[0])]
	else:
		output += ["	Next item in input buffer: none"]
	if len(newState.output):
		output += ["	Last item in output buffer: " + str(newState.output[-1])]
	else:
		output += ["	Last item in output buffer: none"]
	output += ["=============================================="]
	output += []
	output += []
	return output


