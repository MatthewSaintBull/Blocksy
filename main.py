from Block import Block
from Chain import Chain

blockChain = Chain()
block = Block('9bba5f88ec18db7cebe0af644791873762c6838881ebf3eb801a0a3592b77064','blocco numero 1')
val = blockChain.addBlock(block)

block = Block(blockChain.getPreviousHash(),'blocco numero 2');
val = blockChain.addBlock(block)
if(val!=0):
    print("errore con codice : " + str(val))
blockChain.getBlockChain()
