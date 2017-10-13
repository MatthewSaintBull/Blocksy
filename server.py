from flask import Flask
from flask import request
from Chain import Chain
from Block import Block
import json

node = Flask(__name__)
blockChain = Chain()
print(blockChain.startChain().data)


@node.route('/blocks', methods=['GET'])
def blocks():
    chain = blockChain.getBlockChain()
    json_chain=[]
    for block in chain:
        dict = {'hash':block.hash,'id':block.id,'data':block.data}
        json_chain.append(dict)
    return json.dumps(json_chain)



@node.route('/mine',methods=['GET'])
def mine():
    block = Block(blockChain.getPreviousHash(),'Blocco numero 1')
    blockChain.addBlock(block)
    return "BLOCK ADDED SUCCESSFULLY"



node.run(host='0.0.0.0')