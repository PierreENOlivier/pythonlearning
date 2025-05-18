# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json

# Challenge Home 4

def turn_left_n(n: int):    
  for i in range(1, n+1):
    turn_left()        
    
def turn_right():    
  turn_left_n(3)    
  
def move_n(n: int):    
  repeat_move(move, n)
    
def move_L_left():    
  move_n(3)    
  turn_left()
  
def move_L_right():    
  move_n(3)    
  turn_right()    

def next_L():    
  move()    
  turn_right()  

def full_L():    
  move_L_left()    
  move_L_right()    
  next_L()
  
def repeat_move(func, n):  
  for i in range(n):    
    func()
  
# Execute
repeat_move(full_L, 3)
    
move_L_left()

repeat_move(move, 3)

# Challenge 2 - Hurdle 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_left(facing):
	faces = ['right', 'up', 'left', 'down']
	
	if facing not in faces:
		print("Error! Cannot face this direction!")
		exit()
	
	ind = faces.index(facing)
	
	next_ind = ind + 1
	if next_ind > 3:
		next_ind = 0
		
	next_face = faces[next_ind]
	print(f"Facing {next_face}")
	
	return next_face

def repeat_move(func, n):
    for i in range(n):    
    	func()
    
def two_hops():
	repeat_move(move, 2)
	
def turn_right():
	repeat_move(turn_left, 3)
	
# Run hurdles

def turn_right():    
  repeat_move(turn_left, 3)    
  
def repeat_move(func, n):  
  for i in range(n):    
    func()

def make_jump():
	move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def run_race():
	repeat_move(make_jump, 6)
  
# Execute
run_race()

# With while loop
remaining_jumps = 6
while remaining_jumps > 0:
	make_jump()
	remaining_jumps -= 1
	
# With control condition
while not at_goal():
    print(f"Continue running: {not at_goal()}")
    make_jump()
    
    
   
# Around 1 - Variable
run = True
while run:
    if object_here():
        run = False
    else:
        put()
        if not wall_in_front():
            move()
            print ("Keep moving")
        else:
            turn_left()
            print("Turn left")
            move()
    

