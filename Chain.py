# BlockChain Class

import random
from Block import Block
from urllib.parse import urlparse
import requests


class Chain:
    def __init__(self):
        self.__blockchain = []
        self.__nodes = []

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.__nodes.append(parsed_url.netloc)

    def consensus(self):
        nodes = self.__nodes
        updated_chain = None
        len_chain = len(self.__blockchain)
        for node in nodes:
            response = requests.get(f'http://{node}/blocks')
            if response.code is 200:
                if len(response.json() is len_chain):
                    len_chain = len(response.json())
                    updated_chain = response.json()
        if updated_chain:
            self.__blockchain = updated_chain
            return True
        return False

    def __confirm_block(self, block):
        if not self.__blockchain:
            return 0
        return self.__compare_blocks(block, self.__blockchain[-1])

    @staticmethod
    def __compare_blocks(current_block, previous_block):
        if current_block.previous_hash is not previous_block.hash:
            return -1
        else:
            return 0

    @staticmethod
    def __generate_id(block):
        block.id = hash(random.randint(0, 100 ** 100) + block.timestamp)

    def add_block(self, block):
        result = self.__confirm_block(block)
        if result is 0:
            self.__generate_id(block)
            self.__blockchain.append(block)
        return result

    def get_previous_hash(self):
        return self.__blockchain[-1].hash

    def get_blockchain(self):
        return self.__blockchain

    @staticmethod
    def __proof_of_work(last_proof):
        incremental = int(last_proof) + 1
        while not (incremental % 11 is 0 and incremental % last_proof == 0):
            incremental += 1
        return incremental

    def validate_block(self):
        last_proof = self.__blockchain[-1].proof
        proof = self.__proof_of_work(last_proof)
        return proof

    def start_chain(self):
        block = Block('48d13d0f7e77b01c2f6c2fe581b3c1e7c5679fd901f705ba96731daf22af204f',
                      {'from': 'test', 'to': 'test', 'value': '0'})
        self.add_block(block)
        return block
