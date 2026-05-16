from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):

        s = len(self.q)

        self.q.append(x)

        for _ in range(s):
            self.q.append(self.q.popleft())

    def pop(self):

        return self.q.popleft()

    def top(self):

        return self.q[0]

    def empty(self):

        return len(self.q) == 0