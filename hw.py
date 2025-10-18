import math

class Fibonacci:
    def __init__(self, key):
        self.key = key
        self.left = self
        self.right = self
        self.parent = None
        self.child = None
        self.degree = 0
        self.mark = False

class Heap:
    def __init__(self):
        self.min_node = None
        self.total = 0

    def insert(self, key):
        node = Fibonacci(key)
        if self.min_node is None:
            self.min_node = node
        else:
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node
            if node.key < self.min_node.key:
                self.min_node = node
        self.total += 1
        print(f"Inserted key {key}")
        return node

    def get_min(self):
        if self.min_node is None:
            return None
        return self.min_node.key

    def display(self):
        if self.min_node is None:
            print("Heap is empty.")
            return
        print("Root list keys:", end=" ")
        current = self.min_node
        while True:
            print(current.key, end=" ")
            current = current.right
            if current == self.min_node:
                break
        print("\nCurrent minimum:", self.min_node.key)

if __name__ == "__main__":
    fib_heap = Heap()

    fib_heap.insert(10)
    fib_heap.insert(3)
    fib_heap.insert(15)
    fib_heap.insert(6)
    fib_heap.insert(20)

    fib_heap.display()

    print("Minimum element in the Fibonacci Heap:", fib_heap.get_min())

    