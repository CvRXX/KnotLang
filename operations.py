import errors
from errors import succes
from errors import failed
from state import State


def plus(oldState):
	newMemory = oldState.memory
	newMemory[oldState.pointer] += 1
	return succes(State(
		oldState.tokens,
		oldState.pc+1,
		newMemory,
		oldState.pointer,
		oldState.input,
		oldState.output))

def min(oldState):
	newMemory = oldState.memory
	newMemory[oldState.pointer] -= 1
	return succes(State(
		oldState.tokens,
		oldState.pc+1,
		newMemory,
		oldState.pointer,
		oldState.input,
		oldState.output))

def output(oldState):
	newOutput = oldState.output + [oldState.memory[oldState.pointer]]
	return succes(State(
		oldState.tokens,
		oldState.pc+1,
		oldState.memory,
		oldState.pointer,
		oldState.input,
		newOutput))

def pointerPlus(oldState):
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

def pointerMin(oldState):
	if oldState.pointer-1 >= 0:
		return succes(State(
			oldState.tokens,
			oldState.pc+1,
			oldState.memory,
			oldState.pointer-1,
			oldState.input,
			oldState.output))
	else:
		return failed(errors.MemoryOverflow(oldState.pointer-1,oldState.tokens[oldState.pc].knotId))

def input(oldState):
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

def jump(oldState):
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