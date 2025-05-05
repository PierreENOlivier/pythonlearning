rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import randint, choice
game_art = [rock, paper, scissors]
possible_answers = range(3)

play_status = True
while play_status:
	
	ans_player = int(input("What do you choose? Type the number (0) Rock, (1) Paper, (2) Scissors\n"))
	
	
	if ans_player not in possible_answers:
		print("Error! Not a valid entry!")
		exit()
	else:
		print(game_art[ans_player])
	
	ans_machine = choice(possible_answers)
	print(f"Machine played ({ans_machine}):\n")
	print(game_art[ans_machine])
	
	if ans_player == 0 and ans_machine == 2:
		print("You win!")
	elif ans_player == 2 and ans_machine == 0:
		print("You lose!")
	elif ans_player < ans_machine and abs(ans_player - ans_machine) == 1:
		print("You lose!")
	elif ans_player > ans_machine and abs(ans_player - ans_machine) == 1:
		print("You win!")
	elif ans_player == ans_machine:
		print("It's a draw!")
		
	
	ans_continue = input("Play another round? (y)es / (n)o \n").lower()
	if ans_continue not in ['y', 'n']:
		print('Invalid unit!')
	elif ans_continue == "n":
		print("Exiting the game!")
		play_status = False
	else:
		continue
			