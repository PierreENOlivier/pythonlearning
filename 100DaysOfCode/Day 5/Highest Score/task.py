student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

print(f"with sum function {sum(student_scores)}")

total_sum = 0
for score in student_scores:
	total_sum += score

print(f"For loop sum: {total_sum}")

# Get max

print(f"Max func: {max(student_scores)}")

current_max = 0
for score in student_scores:
	# print(f"Score: {score}")
	if score > current_max:
		current_max = score

print(f"Max Loop: {current_max}")
