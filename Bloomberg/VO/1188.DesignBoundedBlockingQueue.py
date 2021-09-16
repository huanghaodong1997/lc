import threading
from collections import deque
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        # Semaphore: if semaphore > 0, you can acquire
        # else you will be block
        self.queue = deque()

        # indicate u can push or not
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)

        # Only one instance can edit the queue at the same time
        self.editing = threading.Lock()
    def enqueue(self, element: int) -> None:
        # -1 pushing capacity
        self.pushing.acquire()
        self.editing.acquire()
        self.queue.append(element)
        self.editing.release()

        # +1 pulling capacity
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
