from typing import List
import functools
import errors
import operations
from errors import expected
from errors import succes
from errors import failed
import state
import visualise



class Token(object):
	def __init__(self,type,value,knotId):
		self.type = type
		self.value = value
		self.knotId = knotId

	def __str__(self):
		return 'Token({type}, {value})'.format(
			type=self.type,
			value=repr(self.value)
			)
	def __repr__(self):
		return self.__str__()


def KLInterpreter(text: str) -> List[str]:
	splittedText = split(text)
	filteredText = list(filter(lambda x: len(x)>0,splittedText))
	parsedTokens=parseTokens(filteredText)
	if parsedTokens.succeeded:
		return interpretTokens(parsedTokens.value)
	else:
		return parsedTokens


def getOutput(state, loggingFunc) -> str:
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
		if loggingFunc:
			loggingFunc(state, result.value)
		return getOutput(result.value, loggingFunc)
	else:
		return result


def run(Interpeter: List[Token],input, debug=False, ramsize: int=5) -> str:
	visualiser = None
	if debug: visualiser = visualise.visualisesStep
	return getOutput(state.init(Interpeter,5,input), visualiser)

def split(data: str) -> str:
	if not len(data):
		return [""]
	if data[0]=="\n":
		return [""] + split(data[1:])
	if data[0]==" ":
		return [""] + split(data[1:])

	appendList = split(data[1:])
	toBeAdded = data[0] + appendList[0]
	return [toBeAdded] + appendList[1:]

def interpretTokens(data):
	if not len(data):
		return succes([])
	if data[0].type == "jumpeq":
		if len(data)<3:
			return failed(errors.UnexpectedEndOfFile(None,data[0].knotId))
		if data[1].type == "connector":
			if data[2].type == "int":
				token = Token("jumpeq",data[2].value,data[0].knotId)
				restOfList = interpretTokens(data[3:])
			else:
				return failed(errors.UnexpectedToken(data[2].type,data[0].knotId))
		else:
			return failed(errors.UnexpectedToken(data[1].type,data[0].knotId))

	elif data[0].type == "connector":
		return failed(errors.UnexpectedToken(data[0].type,data[0].knotId))
	elif data[0].type == "int":
		return failed(errors.UnexpectedToken(data[0].type,data[0].knotId))

	else:
		token = data[0]
		restOfList = interpretTokens(data[1:])

	if restOfList.succeeded:
		return succes([token] + restOfList.value)
	else:
		return restOfList 


def parseTokens(data):
	result = list(map(parseToken,data,range(1,len(data)+1)))
	return errors.mergeErrors(result)
def parseToken(word, id):

	if word == "branch":
		token = Token("jumpeq",None,id)

	elif word == "->":
		token = Token("connector",None,id)

	elif word.isdigit():
		token = Token("int",word,id)

	elif word == "overhand":
		token = Token("+",None,id)

	elif word == "doubleoverhand":
		token = Token("-",None,id)

	elif word == "eight":
		token = Token("output",None,id)

	elif word == "stevedore":
		token = Token("p+",None,id)

	elif word == "ashley":
		token = Token("p-",None,id)

	elif word == "barrelknot":
		token = Token("input",None,id)

	else:
		return failed(errors.UnknownToken(word,id))

	return succes(token)