import knotlang as kl
import sys
sys.setrecursionlimit(15000) # Because looping in functional programming is based on recursion we need a higher limit.

with open('example.kl', 'r') as file:
	data = file.read()
	a = kl.read(data) # We pass a file to the reader
	if a.succeeded: # If the read is succesfull we continue 
		run = kl.run(a.value,[22],False) # We run te program with a list of input vars.
		if run.succeeded: # If it succeeds we continue.
			print(run.value.output) # Output the output buffer.
		else:
			print(run.value) # If running fails show error.
	else:
		print(a.value) # If reading fails show error