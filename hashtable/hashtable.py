class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.size = int(capacity)
        self.storage = [None] * max(capacity, MIN_CAPACITY)
        self.full_slots = 0
        self.resizing = false

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.full_slots % self.size

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # returns the hash value for a key
        # return self.fnv1(key) % self.capacity
        # takes in a key which is also a string
        h = self.djb2(key)
        return h % self.get_num_slots()

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        # convert the key to an integer/hash value
        # check if the index is taken
        # if yes, create a linkedlist to store the key as a pair
        key_index = self.hash_index(key)
        print(key, value, key_index)
        new_node = HashTableEntry(key, value)
        current_node = self.storage[key_index]
        if current_node is None: # which means that the slot is empty right?
        # store the value with its given key
           self.storage[key_index] = new_node
           self.full_slots += 1
        else:
            while current_node.next is not None and current_node.key is not key:
                current_node = current_node.next
            if current_node.key == key:
                current_node.value = value
            else:
                current_node.next = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        # obtain the hash value
        key_index = self.hash_index(key)
        current_node = self.storage[key_index]
        # otherwise proceed with the deletion

        prev_node = None
        while current_node is not None and current_node.key is not key:
            # continue going forward
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("key not found")
            return None
        else:
            deleted_node = current_node.value
            # if the key is the only node in the list
            if prev_node is None:
                self.storage[key_index] = current_node.next
                if current_node.next is None:
                    
            # 1 => 2 => 3 
            # currently pointing to node 2, we want it to point to node 3
            else: prev_node.next = prev_node.next.next

            return deleted_node

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)

        if self.storage[slot] is None:
            print("key not found")
            return None
        # otherwise get the current value
        current_bucket = self.storage[slot]
        while current_bucket is not None:
            if current_bucket.key == key:
                return current_bucket.value
            # handle collisons here
            else:
            raise KeyError('does not exist')

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # the new storage is gotten by increasing the size by 2
        if self.get_load_factor() > 0.7 or self.get_load_factor() < 0.3:
            new_storage = HashTable(self.capacity * 2)
    # copy contents of the old table into the new one


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
