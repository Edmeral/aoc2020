# 14-15 v: vdvvvvvsvvvvvfpv

def is_valid(policy, char, password):
	min = policy[0]
	max = policy[1]
	count = 0
	for c in password:
		if c == char:
			count += 1
		if count > max:
			return False
	if count < min:
		return False
	return True

with open('input.txt', 'r') as f:
	entries = f.read().split('\n')
	entries = entries[0:-1]
	count = 0
	for entry in entries:
		entry = entry.split(' ')
		policy = list(map(lambda n: int(n), entry[0].split('-')))
		char = entry[1][0]
		if is_valid(policy, char, entry[2]):	
			count += 1
	print(count)
