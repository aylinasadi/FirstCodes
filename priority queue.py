class PriorityQueue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item, priority):
        """Add item to the rear of the queue."""
        inserted = False
        for i in range(len(self.items)):
            if self.items[i][1] < priority:
                self.items.insert(i, (item, priority))
                inserted = True
                break
        if not inserted:
            self.items.append((item, priority))

    def dequeue(self):
        """Remove and return the front item. Raise error if empty."""
        if self.is_empty():
            raise IndexError("priority queue is empty")
        return self.items.pop(0)[0]

    def front(self):
        """Return front item without removing. Raise error if empty."""
        if len(self.items) == 0:
            raise IndexError("priority queue is empty")
        return self.items[0][0]

    def is_empty(self):
        """Return True if queue is empty."""
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        """Return number of items in the queue."""
        return len(self.items)
q = PriorityQueue()
q.enqueue("task A", 4)
q.enqueue("task B", 1)
q.enqueue("task C", 3)
q.enqueue("task D", 2)
q.enqueue("task E", 2)
q.dequeue()
q.dequeue()
print(q.front())
print(q.is_empty())
print(q.size())
