from knotlang.datatypes.token import *
from knotlang import errors
from knotlang.errors import succes, failed
from typing import List
from knotlang.errors import expected


# This function reads a string and converts it into a list of words. By splitting it each time it finds an enter or space.
# split::str -> [str]
def split(data: str) -> List[str]:
	if not len(data):
		return [""]
	if data[0]=="\n":
		return [""] + split(data[1:])
	if data[0]==" ":
		return [""] + split(data[1:])

	appendList = split(data[1:])
	toBeAdded = data[0] + appendList[0]
	return [toBeAdded] + appendList[1:]

# Converts a list of words into a list of tokens.
# parseTokens::str->expected{[token],error}
def parseTokens(words: str) -> expected:
	result = list(map(parseToken,words,range(1,len(words)+1)))
	return errors.mergeErrors(result)

# Converts a word in the corosponding token.
# parseToken::str->int->expected{token,error}
def parseToken(word: str, id: int)->expected:

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

# Converts a list of tokens to a new list of tokens with the loop words merged.
# interpretTokens::[Token]->expected{[Token],error}
def interpretTokens(tokens: List[Token])->List[Token]:
	if not len(tokens):
		return succes([])
	if tokens[0].type == "jumpeq":
		if len(tokens)<3:
			return failed(errors.UnexpectedEndOfFile(None,tokens[0].knotId))
		if tokens[1].type == "connector":
			if tokens[2].type == "int":
				token = Token("jumpeq",tokens[2].value,tokens[0].knotId)
				restOfList = interpretTokens(tokens[3:])
			else:
				return failed(errors.UnexpectedToken(tokens[2].type,tokens[0].knotId))
		else:
			return failed(errors.UnexpectedToken(tokens[1].type,tokens[0].knotId))

	elif tokens[0].type == "connector":
		return failed(errors.UnexpectedToken(tokens[0].type,tokens[0].knotId))
	elif tokens[0].type == "int":
		return failed(errors.UnexpectedToken(tokens[0].type,tokens[0].knotId))

	else:
		token = tokens[0]
		restOfList = interpretTokens(tokens[1:])

	if restOfList.succeeded:
		return succes([token] + restOfList.value)
	else:
		return restOfList 


