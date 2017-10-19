from flask import Flask
from flask import request
from Chain import Chain
from Block import Block
import json

node = Flask(__name__)
blockChain = Chain()
blockChain.startChain()
i = 0
transaction_queue = [{'from':'matteo','to':'kevin','value':'3'},{'from':'annie','to':'john','value':'5'}]
blocks_queue = []

@node.route('/blocks', methods=['GET']) #mostra blocchi nella blockchain
def blocks():
    chain = blockChain.getBlockChain()
    json_chain=[]
    for block in chain:
        dict = {'hash':block.hash,'id':block.id,'transaction':block.transactions,'proof':block.proof}
        json_chain.append(dict)
    return json.dumps(json_chain)

@node.route('/addtxion',methods=['GET']) #aggiunge transazione alla coda
def addtxion():
    transaction_queue.append({'from':request.args.get('from'),'to':request.args.get('to'),'value':request.args.get('value')})
    return "TRANSACTION ADDED TO THE QUEUE"

@node.route('/gettxion',methods=['GET']) #mostra transazioni
def getTxion():
    return json.dumps(transaction_queue)

@node.route('/addBlock',methods=['GET']) #aggiunge blocco alla coda dei blocchi da convalidare
def add():
    if not transaction_queue:
        return "YOU DON'T HAVE ANY TRANSACTION TO ADD"
    else:
        if not blocks_queue:
            print("non ci sono blocchi in coda")
            block = Block(blockChain.getPreviousHash(),transaction_queue[:])
        else:
            block = Block(blocks_queue[-1].hash,transaction_queue[:])
        blocks_queue.append(block)
        transaction_queue[:] = []
        return "BLOCK ADDED SUCCESSFULLY"

@node.route('/mine',methods=['GET'])  #valida il blocco e lo aggiunge alla chain
def mine():
    if not blocks_queue :
        return "THERE ARE NO BLOCKS TO MINE"
    else:
        result = blockChain.validateBlock()
        blocks_queue[0].proof = result
        blockChain.addBlock(blocks_queue[0])
        blocks_queue.pop(0)
        print("RIMANGONO : " + str(len(blocks_queue)))

        if not blocks_queue:
            return "BLOCK VALIDATED SUCCESSFULLY "
        else:
            return "BLOCK VALIDATED SUCCESSFULLY : " + json.dumps(blocks_queue[0].transactions)

@node.route('/getBlocks', methods=['GET'])
def getBlockList():
    if not blocks_queue:
        return "there are no blocks in queue"
    else:
        print(tuple(str(i.hash) for i in blocks_queue))
        return str(tuple(str(i.previousHash) for i in blocks_queue))

@node.route('/summary', methods=['GET'])
def summary():
    return "BLOCKCHAIN : "+blocks()+ "TXION : " + getTxion()
node.run(host='0.0.0.0')