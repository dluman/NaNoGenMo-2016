#ROUTINE BORROWS FROM DISCUSSION AT: http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice

import bisect, random

def getChoice(options):
	option, weight = zip(*options)
	total = 0
	weights = []
	for w in weight:
		total += w
		weights.append(total)
	chance = random.random() * total
	result = bisect.bisect(weights,chance)
	return option[result]
