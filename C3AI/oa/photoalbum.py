# O(n ^ 2)
def photoalbum(n, index, identity):
    arr = []
    for i in identity:
        if index[i] >= len(arr):
            arr.append(i)
        else:
            arr.insert(index[i], i)
    return arr
n = 5
index = [0,1,2,1,2]
identity = [0,1,2,3,4]
print(photoalbum(n, index, identity))
        
