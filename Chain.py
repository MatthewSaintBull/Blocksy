#BlockChain Class

import random
from Block import Block
class Chain():
    def __init__(self):
        self.__blockChain = []

    def __validateBlock(self, block):
        if not self.__blockChain: return 0
        return self.__compareBlocks(block,self.__blockChain[-1])

    def __compareBlocks(self, currentBlock,previousBlock):
        if currentBlock.previousHash != previousBlock.hash: return -1
        else: return 0

    def __generateId(self, block):
        block.id = hash(random.randint(0,100**100)+block.timestamp)

    def __generateHash(self, block):
        block.hash = block.calculateHash()

    def addBlock(self, block):
        result = self.__validateBlock(block)
        if result == 0:
            self.__generateId(block)
            self.__generateHash(block)
            self.__blockChain.append(block)
        return result

    def getPreviousHash(self):
        return self.__blockChain[-1].hash

    def getBlockChain(self):
        return self.__blockChain

    def startChain(self):
        block = Block('','STARTING BLOCK')
        self.addBlock(block)
        return block
