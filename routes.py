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
		return 'no available routes...'

	def cheapest_route(self,cost = None):
		if cost is None: cost = self.route_list[0]
		for i in self.route:
			cost=i if i<cost else i
		return cost

	def __str__(self):
		return str(self.routes)

routes = Routes()

def find_route(start = None, end = None):
	if start is None or end is None:
		return 'no routes are found'
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
	route = find_route('a','c')
	print(route)


