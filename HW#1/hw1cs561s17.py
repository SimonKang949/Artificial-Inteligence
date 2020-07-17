import sys
lines = []
nodes = {}
parent = {}
path = []
#with open(sys.argv[2]) as fp:
	#lines.extend(fp.read().splitlines())
#	alg = fp.readline()
#	alg = alg.strip('\n')
#	lines.extend(fp.read().splitlines())
fp = open(sys.argv[2])
fo = open("output.txt","wb")

def generate_graph(lines):
	for line in lines:
		splits = line.split(' ')
		for i in splits:
			if ':' in i:
				node = i.replace(':','')
				#print node
				nodes.setdefault(node,{})
			elif '-' in i:
				temp = i.replace(',','')
				tmp = temp.split('-')
				child = tmp[0]
				cost = int(tmp[1])
				#print child
				#print cost
				tmp_node = nodes[node]
				tmp_node[child] = cost
	#print nodes

def BFS(ini_amount, ini_state, goal_state, lines):
	#define the frontier set
	frontier = []
	#define the explored set
	explored = []
	#generate the graph
	generate_graph(lines)
	#check if the frontier set is empty
	frontier.append(ini_state)
	#print frontier
	temp_node = frontier.pop(0)
	explored.append(temp_node)
	#print temp_node
	left_amount = int(ini_amount)
	#print left_amount
	#loop
	while temp_node != goal_state:
		#flag = 0
		#if len(frontier) == 0:
			#break
		pop_node = nodes[temp_node]
		#print temp_node
		#print pop_node
		for k,v in sorted(pop_node.items()):
			#print k
			if k not in explored:
				if k not in frontier:
					if left_amount-int(v) >= 0:
						#print k
						frontier.append(k)
						#print nodes[k]
						parent.setdefault(k,{})
						tmp = parent[k]
						tmp['parent'] = temp_node
						tmp['left_amount'] = left_amount-int(v)

						#print nodes[k]
						#print parent[k]
			#break
		#print frontier
		#print explored
		if len(frontier) == 0:
			break
		temp_node = frontier.pop(0)
		temp = parent[temp_node]
		left_amount = temp['left_amount']

		#left_amount -= int(pop_node[temp_node])
		explored.append(temp_node)
		#print left_amount
		#if len(frontier) == 0:
			#break
		#break
	#print temp_node
		
	#print parent
	#print parent[goal_state]
	if parent.has_key(goal_state):
		path.append(goal_state)
		check_path = parent[goal_state]
		check_state = check_path['parent']
		while check_state != ini_state:
			path.append(check_state)
			check_path = parent[check_state]
			check_state = check_path['parent']
		path.append(ini_state)
		path.reverse()
	else:
		path.insert(0,'No Path')
	#result = path[::-1]
	#print path


	return 'BFS'

def DFS(ini_amount, ini_state, goal_state, lines):
	frontier = []
	#define the explored set
	explored = []
	#generate the graph
	generate_graph(lines)
	#check if the frontier set is empty
	frontier.append(ini_state)
	#print frontier
	temp_node = frontier.pop()
	explored.append(temp_node)
	#print temp_node
	left_amount = int(ini_amount)

	while temp_node != goal_state:
		#flag = 0
		#if len(frontier) == 0:
			#break
		pop_node = nodes[temp_node]
		temp_reverse = sorted(pop_node.items(),key=lambda item:item[0],reverse=True)
		#print temp_node
		#print pop_node
		for k,v in temp_reverse:
			if k not in explored:
				if left_amount-int(v) >= 0:
					#print k
					frontier.append(k)
					#print nodes[k]
					parent.setdefault(k,{})
					tmp = parent[k]
					tmp['parent'] = temp_node
					tmp['left_amount'] = left_amount-int(v)

						#print nodes[k]
						#print parent[k]
			#break
		if len(frontier) == 0:
			break
		#print frontier
		#print explored
		temp_node = frontier.pop()
		temp = parent[temp_node]
		left_amount = temp['left_amount']

		#left_amount -= int(pop_node[temp_node])
		explored.append(temp_node)
		#print left_amount
		#if len(frontier) == 0:
			#break
		#break
	#print temp_node
	#print frontier
	#print explored
	#print parent
	#print parent[goal_state]
	if parent.has_key(goal_state):
		path.append(goal_state)
		check_path = parent[goal_state]
		check_state = check_path['parent']
		while check_state != ini_state:
			path.append(check_state)
			check_path = parent[check_state]
			check_state = check_path['parent']
		path.append(ini_state)
		path.reverse()
	else:
		path.insert(0,'No Path')

	return 'DFS'

def UCS(ini_amount, ini_state, goal_state, lines):
	frontier = {}
	#define the explored set
	explored = []
	#generate the graph
	generate_graph(lines)
	#check if the frontier set is empty
	frontier[ini_state] = 0
	#print frontier
	temp_node = frontier.keys()[0]
	edge_cost = frontier.pop(temp_node)
	explored.append(temp_node)
	#print temp_node
	left_amount = int(ini_amount)

	#print frontier
	#print explored
	
	while temp_node != goal_state:
		pop_node = nodes[temp_node]

		for k,v in sorted(pop_node.items()):
			if k not in explored:
				if left_amount-int(v) >= 0:
					if k not in frontier.keys():
						frontier[k] = edge_cost + int(v)

						parent.setdefault(k,{})
						tmp = parent[k]
						tmp['parent'] = temp_node
						tmp['left_amount'] = left_amount-int(v)
					else:
						if edge_cost + int(v)<frontier[k]:
							frontier[k] = edge_cost + int(v)

							parent.setdefault(k,{})
							tmp = parent[k]
							tmp['parent'] = temp_node
							tmp['left_amount'] = left_amount-int(v)
						

		if len(frontier) == 0:
			break

		#print frontier
		#print explored

		result = sorted(frontier.items(),key=lambda item:item[1],reverse=False)
		temp_node = result[0][0]
		edge_cost = frontier.pop(result[0][0])
		temp = parent[temp_node]
		left_amount = temp['left_amount']
		explored.append(temp_node)

	if parent.has_key(goal_state):
		path.append(goal_state)
		check_path = parent[goal_state]
		check_state = check_path['parent']
		while check_state != ini_state:
			path.append(check_state)
			check_path = parent[check_state]
			check_state = check_path['parent']
		path.append(ini_state)
		path.reverse()
	else:
		path.insert(0,'No Path')
	return 'UCS'




alg = fp.readline()
alg = alg.strip('\n')
ini_amount = fp.readline().strip('\n')
#fo.write(ini_amount)
#fo.write('\n')
ini_state = fp.readline().strip('\n')
#fo.write(ini_state)
#fo.write('\n')
goal_state = fp.readline().strip('\n')
#fo.write(goal_state)
#fo.write('\n')
lines.extend(fp.read().splitlines())
#for line in lines:
#	fo.write(line)
#	fo.write('\n')

if alg == 'BFS':
	action = BFS(ini_amount, ini_state, goal_state, lines)
	#print path

	if path[0] != 'No Path':
		for i in path:
			if i != goal_state:
				fo.write(i)
				fo.write('-')
			else:
				fo.write(i)
				fo.write(' ')
		j = parent[goal_state]
		k = str(j['left_amount'])
		fo.write(k)
	else:
		fo.write('No Path')
#	for line in lines:
#		fo.write(line)
#		fo.write('\n')
elif alg == 'DFS':
	action = DFS(ini_amount, ini_state, goal_state, lines)
	#print parent
	#print path

	if path[0] != 'No Path':
		for i in path:
			if i != goal_state:
				fo.write(i)
				fo.write('-')
			else:
				fo.write(i)
				fo.write(' ')
		j = parent[goal_state]
		k = str(j['left_amount'])
		fo.write(k)
	else:
		fo.write('No Path')
#	for line in lines:
#		fo.write(line)
#		fo.write('\n')
elif alg == 'UCS':
	action = UCS(ini_amount, ini_state, goal_state, lines)
	#print action
	
	if path[0] != 'No Path':
		for i in path:
			if i != goal_state:
				fo.write(i)
				fo.write('-')
			else:
				fo.write(i)
				fo.write(' ')
		j = parent[goal_state]
		k = str(j['left_amount'])
		fo.write(k)
	else:
		fo.write('No Path')
#	for line in lines:
#		fo.write(line)
#		fo.write('\n')

#fo.write(action)
#fo.write('\n')
fo.close()
fp.close()