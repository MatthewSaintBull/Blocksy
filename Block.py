import time
import hashlib

class Block():
    def __init__(self,previousHash,data):
        self.id = '';
        self.timestamp = int(time.time())
        self.previousHash = previousHash
        self.data = data
        self.hash = ''

    def calculateHash(self):
        hash_string = str(self.id) + str(self.timestamp) + str(self.previousHash) + str(self.data)
        hash = hashlib.sha3_256(hash_string.encode("utf-8")).hexdigest()
        return hash
