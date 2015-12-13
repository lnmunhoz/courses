def has_two(str_n):
	for n in str_n:
		if n is '2':
			return True
	return False

def not_have_seven(str_n):
	for n in str_n:
		if n is '7':
			return False
	return True

count = 0
for n in range(18644, 33088):
	str_n = str(n)
	if has_two(str_n) and have_no_seven(str_n):
		count += 1
print(count)


