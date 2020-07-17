import sys
import copy

#varibles
color_set = []
initial_status = {}
player1_color_score ={}
player2_color_score ={}
depth = 0
lines = []
state_neighbors = {}
explored = {}
frontier = []

best_value = -9999
best_state = ''
best_color = ''

#open files
fp = open(sys.argv[2])
fo = open("output.txt","wb")

#define functions
def get_value(explored):
	#return 0
	#print explored
	player1_score = 0
	player2_score = 0
	for i in explored.keys():
		if explored[i]['player'] == 1:
			color_name = explored[i]['color']
			player1_score = player1_score + player1_color_score[color_name]
			#print player1_color_score[color_name]
		if explored[i]['player'] == 2:
			color_name = explored[i]['color']
			player2_score = player2_score + player2_color_score[color_name]
	leaf_value = player1_score - player2_score
	#print player1_score, player2_score, leaf_value
	return leaf_value


def min_value(state, color, explored, player, cutoff, alpha, beta):
	#cutoff is 0
	global best_color
	global best_state
	if cutoff == 0:
		value_tmp = get_value(explored)
		if alpha == -9999:
			alpha_tmp = '-inf'
		else:
			alpha_tmp = str(alpha)
		if beta == 9999:
			beta_tmp = 'inf'
		else:
			beta_tmp = str(beta)
		fo.write(state+', '+color+', '+str(depth-cutoff)+', '+str(value_tmp)+', '+alpha_tmp+', '+beta_tmp+'\n')
		#print state, color, depth-cutoff
		return value_tmp

	#initial availble state set
	frontier = []
	for i in explored.keys():
		tmp = state_neighbors[i]
		for j in tmp:
			if j in explored.keys():
				continue
			else:
				frontier.append(j)
	frontier = list(set(frontier))
	frontier.sort()
	#print frontier

	v = 9999
	if cutoff == 1:
		for i in frontier:
			availble_color = copy.deepcopy(color_set)
			for j in state_neighbors[i]:
				if j in explored.keys():
					if explored[j]['color'] in availble_color:
						availble_color.remove(explored[j]['color'])
			availble_color.sort()
		if len(availble_color) == 0:
			v = min(v, get_value(explored))
			#return value_tmp

	#initial availble color set
	if alpha == -9999:
		alpha_tmp = '-inf'
	else:
		alpha_tmp = str(alpha)
	if beta == 9999:
		beta_tmp = 'inf'
	else:
		beta_tmp = str(beta)
	if v == 9999:
		v_tmp = 'inf'
	elif v == -9999:
		v_tmp = '-inf'
	else:
		v_tmp = str(v)
	fo.write(state+', '+color+', '+str(depth-cutoff)+', '+v_tmp+', '+alpha_tmp+', '+beta_tmp+'\n')
	#print state, color, depth-cutoff
	for i in frontier:
		availble_color = copy.deepcopy(color_set)
		for j in state_neighbors[i]:
			if j in explored.keys():
				if explored[j]['color'] in availble_color:
					availble_color.remove(explored[j]['color'])
		availble_color.sort()
		#print i, availble_color
		
		for j in availble_color:
			explored_tmp = copy.deepcopy(explored)
			explored_tmp.setdefault(i,{})
			explored_tmp[i]['color'] = j
			player = explored_tmp[state]['player']
			if player == 1:
				player = 2
			elif player == 2:
				player = 1
			explored_tmp[i]['player'] = player
			#print state, color, depth-cutoff
			#print player
			v = min(v, max_value(i,j,explored_tmp,player,cutoff-1,alpha,beta))
			#print state, color, depth-cutoff
			if v <= alpha:
				if alpha == -9999:
					alpha_tmp = '-inf'
				else:
					alpha_tmp = str(alpha)
				if beta == 9999:
					beta_tmp = 'inf'
				else:
					beta_tmp = str(beta)
				if v == 9999:
					v_tmp = 'inf'
				elif v == -9999:
					v_tmp = '-inf'
				else:
					v_tmp = str(v)
				fo.write(state+', '+color+', '+str(depth-cutoff)+', '+v_tmp+', '+alpha_tmp+', '+beta_tmp+'\n')
				return v
			beta = min(beta, v)
			if alpha == -9999:
				alpha_tmp = '-inf'
			else:
				alpha_tmp = str(alpha)
			if beta == 9999:
				beta_tmp = 'inf'
			else:
				beta_tmp = str(beta)
			if v == 9999:
				v_tmp = 'inf'
			elif v == -9999:
				v_tmp = '-inf'
			else:
				v_tmp = str(v)
			fo.write(state+', '+color+', '+str(depth-cutoff)+', '+v_tmp+', '+alpha_tmp+', '+beta_tmp+'\n')
			
	#print state, color, depth-cutoff
	return v


def max_value(state, color, explored, player, cutoff, alpha, beta):
	global best_color
	global best_state
	global best_value
	#cutoff is 0
	if cutoff == 0:
		value_tmp = get_value(explored)
		if alpha == -9999:
			alpha_tmp = '-inf'
		else:
			alpha_tmp = str(alpha)
		if beta == 9999:
			beta_tmp = 'inf'
		else:
			beta_tmp = str(beta)
		fo.write(state+', '+color+', '+str(depth-cutoff)+', '+str(value_tmp)+', '+alpha_tmp+', '+beta_tmp+'\n')
		#print state, color, depth-cutoff
		return value_tmp

	#initial availble state set
	frontier = []
	for i in explored.keys():
		tmp = state_neighbors[i]
		for j in tmp:
			if j in explored.keys():
				continue
			else:
				frontier.append(j)
	frontier = list(set(frontier))
	frontier.sort()
	#print frontier

	v = -9999
	if cutoff == 1:
		for i in frontier:
			availble_color = copy.deepcopy(color_set)
			for j in state_neighbors[i]:
				if j in explored.keys():
					if explored[j]['color'] in availble_color:
						availble_color.remove(explored[j]['color'])
			availble_color.sort()
		if len(availble_color) == 0:
			v = max(v, get_value(explored))
			#return value_tmp

	#initial availble color set	
	if alpha == -9999:
		alpha_tmp = '-inf'
	else:
		alpha_tmp = str(alpha)
	if beta == 9999:
		beta_tmp = 'inf'
	else:
		beta_tmp = str(beta)
	if v == 9999:
		v_tmp = 'inf'
	elif v == -9999:
		v_tmp = '-inf'
	else:
		v_tmp = str(v)
	fo.write(state+', '+color+', '+str(depth-cutoff)+', '+v_tmp+', '+alpha_tmp+', '+beta_tmp+'\n')
	#print state, color, depth-cutoff
	#print explored[state]['player']

	for i in frontier:
		availble_color = []
		availble_color = copy.deepcopy(color_set)
		for j in state_neighbors[i]:
			if j in explored.keys():
				if explored[j]['color'] in availble_color:
					availble_color.remove(explored[j]['color'])
		availble_color.sort()
		#print i, availble_color

		if len(availble_color) == 0 and cutoff == 1:
			v = max(v, get_value(explored))
			#print i, v
			#return value_tmp

		for j in availble_color:
			explored_tmp = copy.deepcopy(explored)
			explored_tmp.setdefault(i,{})
			explored_tmp[i]['color'] = j
			player = explored_tmp[state]['player']
			if player == 1:
				player = 2
			elif player == 2:
				player = 1
			explored_tmp[i]['player'] = player
			#print state, color, depth-cutoff
			#print player
			v = max(v, min_value(i,j,explored_tmp,player,cutoff-1,alpha,beta))
			#v = max(v, min_value(i,j,explored_tmp,player,cutoff-1,alpha,beta))
			if v >= beta:
				if alpha == -9999:
					alpha_tmp = '-inf'
				else:
					alpha_tmp = str(alpha)
				if beta == 9999:
					beta_tmp = 'inf'
				else:
					beta_tmp = str(beta)
				if v == 9999:
					v_tmp = 'inf'
				elif v == -9999:
					v_tmp = '-inf'
				else:
					v_tmp = str(v)
				fo.write(state+', '+color+', '+str(depth-cutoff)+', '+v_tmp+', '+alpha_tmp+', '+beta_tmp+'\n')
				return v
			alpha = max(alpha, v)
			if alpha == -9999:
				alpha_tmp = '-inf'
			else:
				alpha_tmp = str(alpha)
			if beta == 9999:
				beta_tmp = 'inf'
			else:
				beta_tmp = str(beta)
			if v == 9999:
				v_tmp = 'inf'
			elif v == -9999:
				v_tmp = '-inf'
			else:
				v_tmp = str(v)
			fo.write(state+', '+color+', '+str(depth-cutoff)+', '+v_tmp+', '+alpha_tmp+', '+beta_tmp+'\n')
			#print state, color, depth-cutoff
			if depth-cutoff == 0:
				if v > best_value:
					best_value = v
					best_state = i
					best_color = j
	#print state, color, depth-cutoff
	return v


#initial the color set
colors = fp.readline()
colors = colors.strip('\n')
splits = colors.split(',')
for i in splits:
	i = i.replace(' ','')
	#print i
	color_set.append(i)
#print color_set

#initial status
initial = fp.readline()
initial = initial.strip('\n')
splits = initial.split(',')
for i in splits:
	splits2 = i.split(':')
	splits2[0] = splits2[0].replace(' ','')
	initial_state = splits2[0]
	splits2[1] = splits2[1].replace(' ','')
	splits3 = splits2[1].split('-')
	initial_color = splits3[0]
	initial_player = splits3[1]
	#print initial_state
	#print initial_color
	#print initial_player
	initial_status.setdefault(initial_state,{})
	tmp = initial_status[initial_state]
	tmp['color'] = initial_color
	tmp['player'] = int(initial_player)
#print initial_status

#set the depth
depth = int(fp.readline())
#print depth

#player1 preference
line = fp.readline()
splits = line.split(',')
for i in splits:
	i = i.replace(' ','')
	splits2 = i.split(':')
	color_name = splits2[0]
	color_score = splits2[1]
	player1_color_score[color_name] = int(color_score)
#print player1_color_score

#player2 preference
line = fp.readline()
splits = line.split(',')
for i in splits:
	i = i.replace(' ','')
	splits2 = i.split(':')
	color_name = splits2[0]
	color_score = splits2[1]
	player2_color_score[color_name] = int(color_score)
#print player2_color_score

#initial state neighbors
lines.extend(fp.read().splitlines())
for line in lines:
	#print 
	splits = line.split(' ')
	for i in splits:
		#print i
		if ':' in i:
			state = i.replace(':','')
			state_neighbors.setdefault(state,[])
			#print i
		if ':' not in i:
			i = i.replace(',','')
			#print state
			state_neighbors[state].append(i)
		if '' in state_neighbors[state]:
			state_neighbors[state].remove('')
#print state_neighbors

#test
#tmp = state_neighbors['SA']
#for i in tmp:
#	print i
fp.close()

'''
#test
print color_set
print initial_status
print player1_color_score
print player2_color_score
print depth
print state_neighbors
'''
#initial explored set
for i in initial_status.keys():
	#print i
	#print initial_status[i]['color']
	explored.setdefault(i,{})
	tmp = explored[i]
	tmp['player'] = initial_status[i]['player']
	tmp['color'] = initial_status[i]['color']
#print explored

for i in initial_status.keys():
	if initial_status[i]['player'] == 2:
		color = initial_status[i]['color']
		state = i
#print state, color

#print state, color, 0
alpha = -9999
beta = 9999
best_value = max(best_value, max_value(state, color, explored, 1, depth, alpha, beta))

'''
temp = -9999
best_states = next_state.keys()
best_states.sort()
for i in best_states:
	if next_state[i]['value'] == best_value:
		best_state = i
		best_color = next_state[i]['color']
'''

fo.write(best_state+', '+best_color+', '+str(best_value))

fo.close()