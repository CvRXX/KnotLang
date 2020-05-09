from typing import List
import knotlang.datatypes.state
import knotlang.visualise
from knotlang.datatypes.token import *
from knotlang.parsing import *
from knotlang.running import *
from knotlang.errors import expected

# This function reads a string and converts them in tokens. To pass errors an expected type is returned.
# read::int -> expected{[token],error)}
def read(text: str) -> expected:
	splittedText = knotlang.parsing.split(text)
	filteredText = list(filter(lambda x: len(x)>0,splittedText))
	parsedTokens= parseTokens(filteredText)
	if parsedTokens.succeeded:
		return interpretTokens(parsedTokens.value)
	else:
		return parsedTokens

# This function takes a list of tokens and an input buffer and runs it to get the output
# run::[token]->[int]->expected{[int],error}
def run(Interpeter: List[Token],input: List[int], debug: bool=False, ramsize: int=5000) -> expected:
	visualiser = None
	if debug: visualiser = visualise.visualisesStep
	return getOutput(datatypes.state.init(Interpeter,ramsize,input), visualiser)

