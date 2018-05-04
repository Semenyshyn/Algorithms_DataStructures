class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = HashTable.hashfunction(key, self.size)
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key:
            self.data[hashvalue] = data  # replace
        else:
            nexthash = HashTable.rehash(hashvalue)
            while self.slots[nexthash] is not None:
                nexthash = self.rehash(nexthash)
            if self.slots[nexthash] == key:
                self.data = data  # replace
            else:
                self.slots[nexthash] = key
                self.data[nexthash] = data

    def get(self, key):
        hashvalue = HashTable.hashfunction(key, self.size)
        while self.slots[hashvalue] is None or self.slots[hashvalue] != key:
            hashvalue = HashTable.rehash(hashvalue)
        return self.data[hashvalue]

    @staticmethod
    def rehash(old_hash):
        return old_hash + 1

    @staticmethod
    def hashfunction(key, size):
        return key % size

    @property
    def free_indexes(self):
        return [x for x, y in enumerate(self.slots) if y is None]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


hash_t = HashTable()
hash_t[22] = 'test_key_22'
hash_t[23] = 'test_key_23'
hash_t[32] = 'test_key_32'
hash_t[44] = 'test_key_44'
hash_t[22] = 'replace_data'


print(hash_t[22])
print(hash_t[44])
print(hash_t.slots)
print(hash_t.data)
print(hash_t.free_indexes)
