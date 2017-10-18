import time
import hashlib

class Block():
    def __init__(self,previousHash,transaction):
        self.id = '';
        self.timestamp = int(time.time())
        self.previousHash = previousHash
        self.hash = ''
        self.proof = 11
        self.transactions = transaction

    def calculateHash(self):
        hash_string = str(self.id) + str(self.timestamp) + str(self.previousHash) + str(self.transactions)
        hash = hashlib.sha3_256(hash_string.encode("utf-8")).hexdigest()
        return hash
