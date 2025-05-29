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
			cypher += translocate_ind(ind, alpha_lower, translocate_by)
			
		elif let in alpha_upper:
			ind = alpha_upper.find(let)
			print(f"{let}{ind}")
			cypher += translocate_ind(ind, alpha_upper, translocate_by)
			
		else:
			cypher += let
	print(cypher)
	return cypher
			
def translocate_ind(base_ind, cypher, by_n):
	length_cypher = len(cypher)
	
	sum_ind = base_ind + by_n
	if sum_ind > length_cypher:
		over_by = sum_ind - length_cypher
		index0 = over_by - 1
		
		encrypt_let = cypher[index0]

	else:
		encrypt_let =  cypher[sum_ind]
	
	print(f"{cypher[base_ind]}-->{encrypt_let}")
	return encrypt_let

encrypt(secret)
		