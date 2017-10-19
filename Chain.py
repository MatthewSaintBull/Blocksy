#BlockChain Class

import random
from Block import Block
from urllib.parse import urlparse
import requests

class Chain():
    def __init__(self):
        self.__blockChain = []
        self.__nodes = set()

    def register_node(self,address: str) -> None:
        parsed_url = urlparse(address)
        self.__nodes.add(parsed_url.netloc)

    def consensus(self):
        nodes = self.__nodes
        updatedChain = None
        lenChain = len(self.__blockChain)
        for  node in nodes:
            response = requests.get(f'http://{node}/blocks')
            if response.code == 200:
                if len(response.json() > lenChain):
                    lenChain = len(response.json())
                    updatedChain = response.json()
        if updatedChain:
            self.__blockChain = updatedChain
            return True
        return False

    def __confirmBlock(self, block):
        if not self.__blockChain: return 0
        return self.__compareBlocks(block,self.__blockChain[-1])

    def __compareBlocks(self, currentBlock,previousBlock):
        if currentBlock.previousHash != previousBlock.hash: return -1
        else: return 0

    def __generateId(self, block):
        block.id = hash(random.randint(0,100**100)+block.timestamp)


    def addBlock(self, block):
        result = self.__confirmBlock(block)
        if result == 0:
            self.__generateId(block)
            self.__blockChain.append(block)
        return result

    def getPreviousHash(self):
        return self.__blockChain[-1].hash

    def getBlockChain(self):
        return self.__blockChain

    def __proofOfWork(self,last_proof):
        incrementor = int(last_proof) + 1
        while not (incrementor % 11 == 0 and incrementor % last_proof == 0):
            incrementor += 1
        return incrementor

    def validateBlock(self):
        last_proof = self.__blockChain[-1].proof
        proof = self.__proofOfWork(last_proof)
        return proof

    def startChain(self):
        block = Block('48d13d0f7e77b01c2f6c2fe581b3c1e7c5679fd901f705ba96731daf22af204f',{'from':'test','to':'test','value':'0'})
        self.addBlock(block)
        return block
