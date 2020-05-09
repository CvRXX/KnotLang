import kl
import sys
sys.setrecursionlimit(15000)

with open('test.kl', 'r') as file:
	data = file.read()
	a = kl.KLInterpreter(data)
	if a.succeeded:
		run = kl.run(a.value,[22],False)
		if run.succeeded:
			print(run.value.output)
		else:
			print(run.value)
	else:
		print(a.value)