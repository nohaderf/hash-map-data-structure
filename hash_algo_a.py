class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
    
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # insert record into a bucket
    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key,value) # will use last index found in enumerate
        else:
            bucket.append((key,value))
    
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return 'No record found with that email address'
    
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = True
        for index, record in enumerate(bucket):
            if hashed_key == key:
                found_key = True
                break
        if found_key:
            bucket[index].pop
        else:
            return 'No record found with that email address'


    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = AlgoHashTable(256)
hash_table.set_val('freda@example.com', 'some value')
hash_table.set_val('john@wxamplw.com', 'new value')
print(hash_table)
hash_table.set_val('freda@example.com', 'oh, hello')
print(hash_table)
print(hash_table.get_val('hi@gmail.com'))
print(hash_table.delete_val('freda@example.com'))
