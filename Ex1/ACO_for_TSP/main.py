import math
import time

from aco import ACO, Graph
from plot import plot


def distance(city1: dict, city2: dict):
	return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main():
	cities = []
	points = []
	with open('../tsp-instances/instance1.csv') as f:
		index = 1
		for line in f.readlines():
			city = line.split(',')
			cities.append(dict(index=index, x=int(city[0]), y=int(city[1])))
			points.append((int(city[0]), int(city[1])))
			index += 1
	cost_matrix = []
	rank = len(cities)
	for i in range(rank):
		row = []
		for j in range(rank):
			row.append(distance(cities[i], cities[j]))
		cost_matrix.append(row)
	aco = ACO(50, 500, 1.0, 10.0, 0.5, 10, 0)
	graph = Graph(cost_matrix, rank)
	path, cost = aco.solve(graph)
	print('cost: {}, path: {}'.format(cost, path))
	plot(points, path)


if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print("Time elapsed: " + str(round(end - start, 4)) + " seconds")