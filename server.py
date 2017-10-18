from flask import Flask
from flask import request
from Chain import Chain
from Block import Block
import json

node = Flask(__name__)
blockChain = Chain()
blockChain.startChain()

transaction_queue = [{'from':'matteo','to':'kevin','value':'3'},{'from':'annie','to':'john','value':'5'}]
blocks_queue = []

@node.route('/blocks', methods=['GET']) #mostra blocchi nella blockchain
def blocks():
    chain = blockChain.getBlockChain()
    json_chain=[]
    for block in chain:
        dict = {'hash':block.hash,'id':block.id,'transaction':block.transactions}
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
        block = Block(blockChain.getPreviousHash(),transaction_queue[:])
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
        return "BLOCK VALIDATED SUCCESSFULLY"


node.run(host='0.0.0.0')