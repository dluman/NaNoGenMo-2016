from geopy.distance import vincenty

def calcDistance(p1,p2):
	return str(round(vincenty(p1,p2).miles,2))
