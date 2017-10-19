import time
import hashlib
import json


class Block:
    def __init__(self, previous_hash, transaction):
        """

        :rtype: object
        """
        self.id = ''
        self.timestamp = int(time.time())
        self.previous_hash = previous_hash
        self.proof = 11
        self.transactions = transaction
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.id) + str(self.timestamp) + \
            str(self.previous_hash) + str(tuple(self.transactions))
        hash = hashlib.sha3_256(hash_string.encode("utf-8")).hexdigest()
        return hash
