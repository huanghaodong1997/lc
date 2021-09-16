import threading
from collections import deque
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = deque()
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire()
        self.queue.append(element)
        self.editing.release()
        self.pulling.release()
        
    def dequeue(self) -> int:
        val = None
        self.pulling.acquire()
        self.editing.acquire()
        val = self.queue.popleft()
        self.editing.release()
        self.pushing.release()
        return val
    def size(self) -> int:
        return len(self.queue)
