# O(1) visit, O(1) BACK AND FORward, Space O(n)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cursor = 0
        self.end_ptr = 0
    def visit(self, url: str) -> None:
        if self.cursor == len(self.history) - 1:
            self.history.append(url)
            self.cursor += 1
            self.end_ptr += 1
        else:
            self.cursor += 1
            self.end_ptr = self.cursor
            self.history[self.cursor] = url

    def back(self, steps: int) -> str:
        dst = max(0, self.cursor - steps)
        self.cursor = dst
        return self.history[dst]

    def forward(self, steps: int) -> str:
        dst = min(self.end_ptr, self.cursor + steps)
        self.cursor = dst
        return self.history[dst]


# O(n) visit, O(1) BACK AND FORward
# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.history = [homepage]
#         self.cursor = 0
#     def visit(self, url: str) -> None:
#         self.history = self.history[:self.cursor + 1]
#         self.history.append(url)
#         self.cursor += 1

#     def back(self, steps: int) -> str:
#         dst = max(0, self.cursor - steps)
#         self.cursor = dst
#         return self.history[dst]

#     def forward(self, steps: int) -> str:
#         dst = min(len(self.history) - 1, self.cursor + steps)
#         self.cursor = dst
#         return self.history[dst]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)