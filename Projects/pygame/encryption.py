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
			print()
		elif let in alpha_upper:
			print(let)
		else:
			cypher += let
			
def cypher_ind(base_ind, cypher, by_n):
	length_cypher = cypher.len()
	
	sum_ind = base_ind + by_n
	if sum_ind > length_cypher:
		length_cypher - 

encrypt(secret)
		