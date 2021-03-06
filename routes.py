from ordered_set import OrderedSet

nodes = {
	'a':{'b':1,'c':2},
	'b':{'a':1,'c':4,'e':6},
	'c':{'a':2,'b':4,'d':5},
	'd':{'c':5,'f':1,'e':9},
	'e':{'b':6,'d':9,'f':7},
	'f':{'d':1,'e':7},
}

class Routes:
	def __init__(self):
		self.routes = {}
		self.route_number = 0
		self.route_list = OrderedSet()
		self.route = ''

	@property
	def _get_route_list(self):
		return self.route_list

	@property	
	def _get_routes(self):
		return self.routes

	def _add(self,point):
		self.route_list.add(point)
		self.route = '-'.join(self.route_list)

	def _remove(self,point):
		self.route_list.remove(point)

	def _set_route(self):

		def _route_cost(_set,cost = 0):
			_set = list(_set)
			for i in range(len(_set)-1):
				if any(_set[i+1]==k for k in nodes[_set[i]].keys()):
					cost+=nodes[_set[i]][_set[i+1]]
			return cost

		if len(self.route)>1:
			result = self.route
			if result not in self.routes.values():
				self.route_number+=1
				cost = _route_cost(self.route_list)
				self.routes[self.route_number] = result,cost
				self.route_list = self.route_list[:-1]
				self.route = ''

	@staticmethod
	def cheapest_route(routes):
		cost = tuple()
		if routes:
			values = routes.values()
			value_iter = iter(values)
			cost = next(value_iter)
			c = cost[1]
			for i in routes.keys():
				if c>routes[i][1]:
					c=routes[i][1]
					cost[0] = routes.get(i)[0]
			return f'cheapest route is: {cost}'
		return f'There is not routes...'

	def __str__(self):
		return str(self.routes)

routes = Routes()

def find_route(start = None, end = None):
	if start is None or end is None:
		return
	routes._add(start)
	if start == end:
		result = routes._get_routes
		routes._remove(end)
		return result
	if end in nodes[start].keys():
		routes._add(end)
		routes._set_route()	
	for point in nodes[start].keys():
		if point not in routes._get_route_list:
			find_route(point,end)
		continue
	return routes._get_routes


if __name__ == '__main__':
	route = find_route('d','c')
	print(route)
	cheapest_one = routes.cheapest_route(route)
	print(cheapest_one)


