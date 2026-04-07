class HashTable:
    def __init__(self, size=40):
        # Create empty bucket for each package(40 packages)
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, package_id, package):
        index = package_id % self.size
        bucket = self.table[index]

        # Check if package already exists.. if it does then update it
        for i in range(len(bucket)):
            key, value = bucket[i]
            if key == package_id:
                bucket[i] = (package_id, package)
                return

        # If not found, append new package
        bucket.append((package_id, package))

    def lookup(self, package_id):
        index = package_id % self.size
        bucket = self.table[index]

        for key, package in bucket:
            if key == package_id:
                return package

        return None