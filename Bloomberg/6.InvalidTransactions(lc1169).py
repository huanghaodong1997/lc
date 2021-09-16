class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = time
        self.amount = amount
        self.city = city
    def to_string(self):
        return ",".join([self.name, str(self.time), str(self.amount), self.city])

class Solution:
    def invalidTransactions(self, transactions) :
        n = len(transactions)
        def parse(transaction):
            res = []
            prev = curr = 0
            while len(res) < 3:
                curr = transaction.index(',', curr)
                res.append(transaction[prev:curr])
                prev = curr + 1
                curr = curr + 1
            res.append(transaction[curr:])
            return res
        ts = []
        for t in transactions:
            name, time, amount, city = parse(t)
            ts.append(Transaction(name, int(time), int(amount), city))
        ts.sort(key=lambda x:x.time)
        
        invalid = [False] * n
        for i in range(n):
            curr_t = ts[i]
            if curr_t.amount > 1000: invalid[i] = True
            for j in range(i + 1, n):
                next_t = ts[j]
                if curr_t.name == next_t.name and curr_t.city != next_t.city and abs(next_t.time - curr_t.time) <= 60:
                    invalid[j] = True
                    invalid[i] = True
        res = []
        for i in range(n):
            if invalid[i]: res.append(ts[i].to_string())
        return res
        