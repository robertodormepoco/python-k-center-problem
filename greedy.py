import random;
import pylab as plt
import numpy as np
import time

def main():
        min = 0
        max = 800
        vertexes = set()
        for i in range(0, 8):
                vertexes.add(randomVertex(min, max))

	print len(vertexes)
	
	s_greedy = greedy(vertexes, 3)
	
        points = []

        for v in vertexes:
                points.append(v.points())

        x_list = [x for [x, y] in points]
        y_list = [y for [x, y] in points]

        plt.plot(x_list, y_list, "ro")

	s_points = []
	
	for s in s_greedy:
		s_points.append(s.points())

	x_greedy = [x for [x, y] in s_points]
	y_greedy = [y for [x, y] in s_points]

	plt.plot(x_greedy, y_greedy, "bo")

        plt.show()	

def greedy(vertexes, k):
	s = [];
	pick = randomPick(vertexes);
	s.append(pick)
	print pick
	while len(s) < k:
		max = distance(vertexes, s)
		vertexes.remove(max)
		s.append(max)
	return s


def randomPick(vertexes):
	# rndm plz ;)
	return vertexes.pop();

def distance(vertexes, picked):
	max = 0
	max_v = None
	real_max = 0
	real_max_v = None
	for v in vertexes:
		for p in picked:	
			d = np.sqrt((v.x - p.x)**2 + (v.y - p.y)**2)
			print ("from %s to %s: %s" % (p, v, d))
			if d > max:
				max = d
				max_v = v
		if max > real_max:
			real_max = max
			real_max_v = max_v
			
	print real_max, real_max_v

	return real_max_v
	
def randomVertex(min, max):
	return Vertex(random.randint(min, max), random.randint(min, max))

class Vertex:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%s,%s)" % (self.x, self.y)

	def __repr__(self):
                return "(%s,%s)" % (self.x, self.y)

	def points(self):
		return [self.x, self.y]

if __name__ == "__main__":
	main()
