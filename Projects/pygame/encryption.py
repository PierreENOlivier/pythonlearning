# Cypher - Message Encryption and Decryption

import string as ss

alpha_lower = ss.ascii_lowercase
alpha_upper = ss.ascii_uppercase

print(alpha_lower)

secret = input("What is your secret message?\n")

def encrypt(text: str):
	cypher = ""
	translocate_by = 13
	for let in secret:
		if let in alpha_lower:
			ind = alpha_lower.find(let)
			print(f"{let}{ind}")
			cypher += translocate_ind(ind, alpha_lower, translocate_by, 'forward')
			
		elif let in alpha_upper:
			ind = alpha_upper.find(let)
			print(f"{let}{ind}")
			cypher += translocate_ind(ind, alpha_upper, translocate_by, 'forward')
			
		else:
			cypher += let
	print(cypher)
	return cypher
			
def translocate_ind(
		base_ind: int,
		cypher: str,
		by_n: int = 13,
		direction: str = ['forward', 'backward']):
	length_cypher = len(cypher)

	if direction == 'forward':
		sum_ind = base_ind + by_n
		if sum_ind > length_cypher:
			over_by = sum_ind - length_cypher

			shifted_let = cypher[over_by]

		else:
			shifted_let = cypher[sum_ind]

		print(f"{cypher[base_ind]}-->{shifted_let}")

	else:
		sum_ind = base_ind - by_n
		if sum_ind < 0:
			over_by = sum_ind - length_cypher

			shifted_let = cypher[over_by]

		else:
			shifted_let = cypher[sum_ind]

		print(f"{cypher[base_ind]}-->{shifted_let}")


	return shifted_let

encrypt(secret)


		