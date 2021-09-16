import math
# bf
def memleak(M1, M2):
    times = 0

    while True:
        if times > max(M1, M2): break
        if M1 >= M2:
            M1 -= times
        else:
            M2 -= times
        times += 1
    return (times, M1, M2)


# math
def get_n(start,sum_num):
	n = int(math.sqrt(2*sum_num))-start
	while True:
		# print(n)
		if get_sum(start,n) > sum_num:
			break
		n += 1
	return n-1

def get_sum(start,n):
	return (start+start+2*n-2)*n//2

def memleak_math(M1, M2):
    A = M1 if M1 >= M2 else M2
    B = M2 if M1 >= M2 else M1
    swap = True if M1 < M2 else False
    t = 0
    if A > B:
        diff = A - B
        min_step = int(math.sqrt(2 * diff))
        t = min_step
        A -= (t * (1 + t) // 2)
        if A == B: swap = False
    if A == B:
        t1 = get_n(t + 1, A)
        t2 = t1 - 1 if t1 > 0 else 0
        print(t1, t2)
        A -= get_sum(t + 1, t1)
        B -= get_sum(t + 2, t2)
        t += (t1 + t2 + 1)
    #elif A < B:

    return (t, A, B) if not swap else (t, B, A)

    #print(t, A, B)



print(memleak_math(2, 2))

tc_1 = [(18, 395), (1063, 910), (5731, 8232), (46157, 97733), (733477, 399112), (8143979, 8145574), (94418021, 94416251), (397273819, 906480582), (9101619295, 7146478457), (35750588456, 12317418803), (725116106598, 725116108613), (8208225874844, 8208225874739), (21586949555841, 86676934485993), (859371661172885, 650174488915793), (1685506627927479, 6657174379437870)]

for m1, m2 in tc_1:
    t, a, b = memleak(m1,m2)
    print(t,a,b)