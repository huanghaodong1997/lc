from collections import Counter
arr = [2,3,1,3,2]

def canyousort(arr):
    c = Counter(arr)
    a = sorted([(c[i], i) for i in arr])
    return [num for _, num in a]

print(canyousort(arr))
