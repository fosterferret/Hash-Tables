# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        index = self._hash_mod(key)
        node = LinkedPair(key, value)
        node.next = self.storage[index]
        self.storage[index] = node

        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        #     return

        # self.storage[index] = LinkedPair(key, value)
        # pass

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        next_node = None

        while node is not None and node.key != key:
            next_node = node
            node = next_node.next

        if node is None:
            print("Node not found")

        else:
            if next_node is None:
                self.storage[index] = node.next
            else:
                next_node.next = node.next
        self.count -= 1

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        head = self.storage[index]

        while head:
            if head.key == key:
                return head.value
            head = head.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        storage = self.storage
        capacity = self.capacity
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for i in range(capacity):
            curr = storage[i]
            if curr is None:
                continue
            while curr.next:
                self.insert(curr.key, curr.value)
                curr = curr.next
            self.insert(curr.key, curr.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
