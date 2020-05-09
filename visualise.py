def visualisesStep(oldState, newState):
	print("==============================================")
	print("Current state:")
	if oldState.pc==len(oldState.tokens):
		print("	Next action: none")
	else:
		print("	Next action: " + oldState.tokens[oldState.pc].type)
	print("	Current pointeraddress: " + str(oldState.pointer))
	print("	Current value at pointer: " + str(oldState.memory[oldState.pointer]))
	if len(oldState.input):
		print("	Next item in input buffer: " + str(oldState.input[0]))
	else:
		print("	Next item in input buffer: none")
	if len(oldState.output):
		print("	Last item in output buffer: " + str(oldState.output[-1]))
	else:
		print("	Last item in output buffer: none")
	print()
	print("After action:")
	if oldState.pc>=len(oldState.tokens)-1:
		print("	Next action: none")
	else:
		print("	Next action: " + newState.tokens[newState.pc].type)
	print("	Current pointeraddress: " + str(newState.pointer))
	print("	Current value at pointer: " + str(newState.memory[newState.pointer]))
	if len(newState.input):
		print("	Next item in input buffer: " + str(newState.input[0]))
	else:
		print("	Next item in input buffer: none")
	if len(newState.output):
		print("	Last item in output buffer: " + str(newState.output[-1]))
	else:
		print("	Last item in output buffer: none")
	print("==============================================")
	print()
	print()


