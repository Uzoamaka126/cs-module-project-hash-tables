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
    def __init__(self, capacity):
        # Your code here
        # if capacity >= MIN_CAPACITY:
        #     # then initialize an empty list with None values
        self.capacity = capacity
        self.storage = [None] * capacity

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
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # returns the hash value for a key
        #return self.fnv1(key) % self.capacity
        # takes in a key which is also a string
        return self.djb2(key) % self.get_num_slots()

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
        slot = self.hash_index(key)
        if not self.storage[slot]:
            self.storage[slot] = HashTableEntry(key, value)
        # store the value with its given key
        else:
            current_bucket = self.storage[slot]
            while current_bucket:
                if current_bucket.key == key:
                    current_bucket.value = value
                    break
                elif current_bucket.next:
                    current_bucket = current_bucket.next
                else:
                    break
            current_bucket.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # obtain the hash value
        slot = self.hash_index(key)
        if self.capacity[slot] is None:
            print("key not found")
            return
        # otherwise proceed with the deletion
        self.capacity[slot] == None
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # get the index of the particular key
        selected_key = self.hash_index(key)

        if not self.storage[selected_key]:
            return None
        # otherwise get the current value
        while self.storage[selected_key] is not None:
            if self.storage[selected_key].key == key:
                return self.storage[selected_key].value
            # go to the next index by increasing it by 1
            elif self.storage[selected_key].next != None:
                self.storage[selected_key] = self.storage[selected_key].next
            else:
                return None

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # the new storage is gotten by increasing the size by 2
        new_storage = HashTable(self.capacity * 2)




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
