def repeat_move(func, n):
  for i in range(n):    
    func()

def turn_left(facing):
	faces = ['right', 'up', 'left', 'down']
	
	if facing not in faces:
		print("Error! Cannot face this direction!")
		exit()
	
	print(f"Facing {facing}")
	
	ind = faces.index(facing)
	
	next_ind = ind + 1
	if next_ind > 3:
		next_ind = 0
		
	next_face = faces[next_ind]
	print(f"Now facing {next_face}!")
	
	return next_face
	
def turn_right(facing):
	faces = ['right', 'up', 'left', 'down']
	ind_right = faces.index("right")
	
	current_ind = faces.index(facing)
	
	n_turns = current_ind - ind_right
	
	repeat_move(turn_left(facing), n_turns)
	
turn_right("left")