import math
import random

def get_n(start,sum_num):
	n = int(math.sqrt(2*sum_num))-start
	while True:
		# print(n)
		if get_sum(start,n) > sum_num:
			break
		n += 1
	return n-1

def get_sum(start,n):
	return (start+start+2*n-2)*n/2
print(get_sum(3, 0))
# for i in range(10):
# 	start = random.randint(1,1000)
# 	inc = random.randint(1,1000)
# 	gn = get_n(start, start+inc)
# 	s1 = get_sum(start, gn)
# 	s2 = get_sum(start, gn+1)
# 	print('start', start, 'goal', start+inc, 'n', gn, 'calculated_sum', s1, s2)
# def get_whos_first(a,b):
# 	diff1 = a-b
# 	n = int(math.sqrt(diff1))
# 	first_sum = (1+n)*n/2
# 	a -= first_sum
# 	more_steps = get_n(n+2, b)
# 	a_sum = (n+1+2*more_steps-2)*more_steps/2
# 	a_left = a-a_sum
# 	return n+more_steps

# print(get_whos_first(11,8))