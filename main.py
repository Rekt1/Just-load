import time
import random
import itertools

rndm = random.uniform(.10,.5)

for i in range(100):
	byt = random.randint(1, 1030)
	time.sleep(rndm)
	if byt >= 1024:
		print("█"*i, str(1)+" кб/сек")
	else:
		print("█"*i, str(byt)+" мб/сек")
print("\nDone")

it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3 )

for x in range(30):
	time.sleep(.3)
	print(next(it), end="", flush="True")
print("\nDone")