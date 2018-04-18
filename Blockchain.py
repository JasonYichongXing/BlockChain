#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:21:05 2018

@author: xingyichong
"""

import hashlib
import datetime

INIT_DIFFICULTY = 2
MAX_NONCE = 2**16

INIT_BlOCKNO = 0
INIT_INFO = None
INIT_NNONCE = 0
INIT_PREV_HASH = 0
INIT_TIMESTAMP = datetime.datetime(2018, 4, 17)


class Block:
        
    def __init__(self, Transaction_info = INIT_INFO):
        self.BlockNo = INIT_BlOCKNO
        self.nTime = INIT_TIMESTAMP
        self.previous_hash = INIT_PREV_HASH
        self.Nonce = INIT_NNONCE
        self.Info = Transaction_info
       
        self.Hash = self.GetHash()   

        
    def GetHash(self):
        h = hashlib.sha256()
        h.update(
            bytes(str(self.BlockNo) +
                  str(self.Info) +
                  str(self.nTime) +
                  str(self.previous_hash) +
                  str(self.Nonce), 'utf-8'))
        return h.hexdigest()
        
    
    def __str__(self):
        return '\nBlock No: ' + str(self.BlockNo) + '\nBlock Hash: ' + str(self.GetHash()) + '\nPrevius Hash: ' + str(self.previous_hash) + '\nNonce: ' + str(self.Nonce) + '\nTransaction Info: ' + str(self.Info) + '\n============\n'

####################################
        
def proof_of_work(block, Diff = INIT_DIFFICULTY):
    Diff_string = ''.join(['0' for _ in range(Diff)])
    return block.GetHash()[:Diff] == Diff_string


def BlockChain_gen(N):
    BlockChain = []
    
    Genesis = Block('Genesis Block')
    
    BlockChain.append(Genesis)
    
    assert proof_of_work(Genesis) == False or INIT_DIFFICULTY ==0
    assert proof_of_work(Genesis, 0) == True 

    for n in range(1, N+1):
        Block_add = Block('Block #' + str(n))
        Block_add.BlockNo = n
        Block_add.previous_hash = BlockChain[-1].GetHash()
    
        i = 1
        while i < MAX_NONCE:
            if proof_of_work(Block_add):
                BlockChain.append(Block_add)
                break
            
            else:
                Block_add.Nonce += 1      
            i += 1
    return BlockChain

'''
for _ in BlockChain_gen(10):
    print(_)
'''
    
x = BlockChain_gen(20)

for _ in BlockChain_gen(20):
    print(_.BlockNo, ': ', _.GetHash())



