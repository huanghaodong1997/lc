words = ["cat", "cat", "bat", "tab", "ttbb"]
orders = ["c", "b", "a", "t"]

def compare_words(word, other, order:dict) -> int:

    for i in range(0, min(len(word), len(other))):
        if order[word[i]] < order[other[i]]:
            return -1
        elif order[word[i]] > order[other[i]]:
            return 1
    if len(word) == len(other):
        return 0
    elif len(word) > len(other):
        return -1
    else:
        return 1

def compare(words, orders):
    if len(words) <= 1: return True

    order = {}
    for i, ch in enumerate(orders):
        order[ch] = i

    for i in range(0, len(words) - 1):
        word, other = words[i], words[i + 1]
        if compare_words(word, other, order) == 1:
            return False
    return True

print(compare(words, orders))