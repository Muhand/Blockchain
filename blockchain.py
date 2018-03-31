# A simple general puprose blockchain
# This requires Python 3.5+

#Dependencies
# 1 - Flask==0.12.2: pip install Flask==0.12.2 or pip3 install Flask==0.12.2

#Importing liabraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

#Building the chain
class Blockchain:
    
    #Constructor
    def __init__(self):
        #Initialize the chain
        self.chain = []                                                        # A list which will contain all the blocks
        self.create_block(proof = 1, previous_hash = '0')                      # The genesis block (The first block in a chain) which will start with proof 1 and no previous hash
        
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        
        #Append the created block to the chain
        self.chain.append(block)
        
        #Return the block
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1                                                          # Start the proof at 1 and keep increasing until we reach a solution
        correct_proof = False
        
        while correct_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] == '0000':
                correct_proof = True
            else:
                new_proof += 1
                
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len(chain):
            current_block = chain[block_index]
            if current_block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_proof = previous_block['proof']
            proof = current_block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] != '0000':
                return False
            
            previous_block = current_block
            block_index += 1
            
        return True
            
            

#Mining the chain
        