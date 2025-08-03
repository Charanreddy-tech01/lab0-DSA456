class ChainingTable:
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
        self.table = [[] for _ in range(capacity)]
        self.cap = capacity
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.cap

    def _grow(self):
        old_table = self.table
        self.cap *= 2
        self.table = [[] for _ in range(self.cap)]
        for chain in old_table:
            for record in chain:
                idx = self._hash(record.key)
                self.table[idx].append(record)

    def insert(self, key, value):
        if self.search(key) is not None:
            return False
        if (self.count + 1) / self.cap > 1.0:
            self._grow()
        idx = self._hash(key)
        self.table[idx].append(self.Record(key, value))
        self.count += 1
        return True

    def modify(self, key, value):
        idx = self._hash(key)
        for record in self.table[idx]:
            if record.key == key:
                record.value = value
                return True
        return False

    def remove(self, key):
        idx = self._hash(key)
        chain = self.table[idx]
        for i, record in enumerate(chain):
            if record.key == key:
                del chain[i]
                self.count -= 1
                return True
        return False

    def search(self, key):
        idx = self._hash(key)
        for record in self.table[idx]:
            if record.key == key:
                return record.value
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.count


if __name__ == "__main__":
    table = ChainingTable()
    print("Inserting key1:", table.insert("key1", "value1"))
    print("Inserting key2:", table.insert("key2", "value2"))
    print("Inserting key1 again:", table.insert("key1", "value3"))
    print("Search key1:", table.search("key1"))
    print("Modify key2:", table.modify("key2", "updated"))
    print("Search key2:", table.search("key2"))
    print("Remove key1:", table.remove("key1"))
    print("Search key1:", table.search("key1"))
    print("Length:", len(table))
    print("Capacity:", table.capacity())
