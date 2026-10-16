class ListNode:
    def __init__(self, key=None, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.c = capacity
        self.head = ListNode(0)

    def get(self, key: int) -> int:
        if key not in self.lru:
            # print(key)
            # print(self.lru)
            return -1

        # Disconnect the current node's prev and next
        node = self.lru[key]
        if len(self.lru) > 1:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            # Move node to the front
            node.next = self.head.next
            node.prev = self.head
            node.next.prev = node
            self.head.next = node
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # Input the key into dict or update the key's value
        if key in self.lru:
            node = self.lru[key]
            node.val = value
            print(f'{key} is returning')
            if len(self.lru) > 1:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            # Move node to the front
            node.next = self.head.next
            node.prev = self.head
            node.next.prev = node
            self.head.next = node
        else:
            # Create a new node and put it in the dict
            newNode = ListNode(key, value, prev = self.head)
            self.lru[key] = newNode

            # Check to see if the dict is longer than capacity 
            if len(self.lru) > self.c:
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.prev.next = None
                curr.next = None
                del self.lru[curr.key]
        
            # Add new node to list
            if len(self.lru) > 1:
                newNode.next = self.head.next
                newNode.next.prev = newNode
                self.head.next = newNode
            else:
                newNode.next = self.head.next
                self.head.next = newNode


