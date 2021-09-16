def ngrams(input, n):
    input = input.split(' ')
    output = []
    q = input[0:n]
    output.append(q[:])
    for i in range(n, len(input)):
        q.pop(0)
        q.append(input[i])
        output.append(q[:])    
    print("LENGTH " + str(len(output)))
    return output


def countNGrams(input, n):
    input = input.split(' ')
    return len(input) - n + 1
#print(ngrams('a b c d e f g h', 4))
#print(countNGrams('a b c d e f g h', 4))

# 1.2 given string[], k and target phrase, return the count of all 1-k grams that start with the target phrase

def count1ToKGrams(input, k, target):
    input = input.split(' ')
    n = len(input)
    res = 0
    for i, phrase in enumerate(input):
        if input[i] == target:
            res += min(n - i, k)
    return res

print(count1ToKGrams('a a a c e f g a', 2, 'a'))