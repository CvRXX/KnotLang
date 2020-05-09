import knotlang.errors
from knotlang.errors import succes
from knotlang.errors import failed
from knotlang.datatypes.state import State
from knotlang.errors import expected
from knotlang import errors


# Increments the current byte by one and returns state.
# plus::State->expected{State,error}
def plus(oldState: State)->expected:
	newMemory = oldState.memory
	newMemory[oldState.pointer] += 1
	return succes(State(
		oldState.tokens,
		oldState.pc+1,
		newMemory,
		oldState.pointer,
		oldState.input,
		oldState.output))

# Decrements the current byte by one and returns state.
# min::State->expected{State,error}
def min(oldState: State)->expected:
	newMemory = oldState.memory
	newMemory[oldState.pointer] -= 1
	return succes(State(
		oldState.tokens,
		oldState.pc+1,
		newMemory,
		oldState.pointer,
		oldState.input,
		oldState.output))

# Appends the current byte to the output buffer and returns state.
# output::State->expected{State,error}
def output(oldState: State)->expected:
	newOutput = oldState.output + [oldState.memory[oldState.pointer]]
	return succes(State(
		oldState.tokens,
		oldState.pc+1,
		oldState.memory,
		oldState.pointer,
		oldState.input,
		newOutput))

# Increments the pointer by one and returns state.
# pointerPlus::State->expected{State,error}
def pointerPlus(oldState: expected):
	if oldState.pointer+1 < len(oldState.memory):
		return succes(State(
			oldState.tokens,
			oldState.pc+1,
			oldState.memory,
			oldState.pointer+1,
			oldState.input,
			oldState.output))
	else:
		return failed(errors.MemoryOverflow(oldState.pointer+1,oldState.tokens[oldState.pc].knotId))

# Decrements the pointer by one and returns state.
# pointerMin::State->expected{State,error}
def pointerMin(oldState: State)->expected:
	if oldState.pointer-1 >= 0:
		return succes(State(
			oldState.tokens,
			oldState.pc+1,
			oldState.memory,
			oldState.pointer-1,
			oldState.input,
			oldState.output))
	else:
		return failed(errors.MemoryUnderflow(oldState.pointer-1,oldState.tokens[oldState.pc].knotId))

# Takes the next byte from the inputbuffer and put it on the current byte and returns state.
# input::State->expected{State,error}
def input(oldState: State)->expected:
	if not len(oldState.input):
		return failed(errors.InputEmpty(oldState.tokens[oldState.pc].knotId))
	newMemory = oldState.memory
	newMemory[oldState.pointer] = oldState.input[0]
	return succes(State(
		oldState.tokens,
		oldState.pc+1,
		newMemory,
		oldState.pointer,
		oldState.input[1:],
		oldState.output))

# If the current byte is higher than 0 jump to jumpvalue and return state.
# jump::State->expected{State,error}
def jump(oldState: State)->expected:
	if oldState.memory[oldState.pointer]>0:
		toJumpTo = int(oldState.tokens[oldState.pc].value)-1
		
		if toJumpTo < 0:
			return failed(errors.JumpUnderflow(toJumpTo+1,oldState.tokens[oldState.pc].knotId))
		elif not toJumpTo < len(oldState.tokens):
			return failed(errors.JumpOverflow(toJumpTo+1,oldState.tokens[oldState.pc].knotId))
		else:
			return succes(State(
				oldState.tokens,
				toJumpTo,
				oldState.memory,
				oldState.pointer,
				oldState.input,
				oldState.output))
	else:
		return succes(State(
				oldState.tokens,
				oldState.pc+1,
				oldState.memory,
				oldState.pointer,
				oldState.input,
				oldState.output))