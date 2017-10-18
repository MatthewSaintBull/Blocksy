import time
import hashlib
import json
class Block():
    def __init__(self,previousHash,transaction):
        self.id = '';
        self.timestamp = int(time.time())
        self.previousHash = previousHash
        self.proof = 11
        self.transactions = transaction
        self.hash = self.calculateHash()

    def calculateHash(self):
        hash_string = str(self.id) + str(self.timestamp) + str(self.previousHash) + str(tuple(self.transactions))
        hash = hashlib.sha3_256(hash_string.encode("utf-8")).hexdigest()
        return hash
