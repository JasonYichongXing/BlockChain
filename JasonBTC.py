#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:21:05 2018

@author: xingyichong
"""
import hashlib
import datetime

from MkTreeClass import MerkleTree as MK


INIT_DIFFICULTY = 2
MAX_NONCE = 2**32

INIT_BlOCKNO = 0
INIT_INFO = ()
INIT_NNONCE = 0
INIT_PREV_HASH = 0
INIT_TIMESTAMP = datetime.datetime(2018, 4, 17)


class Block:
        
    def __init__(self, Transaction_info=INIT_INFO):
        self.BlockNo = INIT_BlOCKNO
        self.nTime = INIT_TIMESTAMP
        self.previous_hash = INIT_PREV_HASH
        self.Nonce = INIT_NNONCE
        self.Info = Transaction_info
        
    @property   
    def Hash(self): 
        return self.GetHash()   

    @property
    def MerkleRoot(self):
        return MK.get_root(self.Info)
        
           
    def GetHash(self):
        h = hashlib.sha256()
        h.update(
            bytes(str(self.BlockNo) +
                  str(self.Info) +
                  str(self.nTime) +
                  str(self.previous_hash) +
                  str(self.MerkleRoot) +
                  str(self.Nonce), 'utf-8'))
        return h.hexdigest()

    def __str__(self):
        return '\nBlock No: ' + str(self.BlockNo) + '\nBlock Hash: ' + str(self.Hash) + '\nPrevius Hash: ' + str(self.previous_hash) + '\nMerkleRoot: ' + str(self.MerkleRoot) + '\nNonce: ' + str(self.Nonce) + '\nTransaction Info: ' + str(self.Info) + '\n============\n'



#######################################
        
def is_PoW(block, Diff=INIT_DIFFICULTY):
    """ return the hash once Prove_of_Work is confirmed under current difficulty."""
    
    Diff_string = ''.join('0' for _ in range(Diff))
    return block.Hash[:Diff] == Diff_string


def create_Genesis(BlockChain):
    """ to create the Genesis block on a given empty chain."""
    
    if BlockChain:
        raise ValueError('\nThe Inital BlockChain should be empty, before create Genesis Block!')
    Genesis = Block(('Genesis Block', 'This is the first one'))
    BlockChain.append(Genesis)   
    return BlockChain


def generate_newBlock(prev_block, new_Transaction):
    """ the new transaction info to be added must be a tuple for here."""
    
    newBlock = Block(new_Transaction)
    
    newBlock.BlockNo = prev_block.BlockNo + 1
    newBlock.previous_hash = prev_block.Hash
    
    while not is_PoW(newBlock) and newBlock.Nonce < MAX_NONCE:
        newBlock.Nonce += 1
        
    return newBlock


def Generate_BlockChain(N):
    """to generate a Chain with N blocks on a Genesis Block"""

    BlockChain = []
    create_Genesis(BlockChain)
    
    for n in range(1, N+1):
        newBlk = generate_newBlock(BlockChain[-1], ({'Name':'Block #'+ str(n), 'Amount': n*1000}))
        BlockChain.append(newBlk)

    return BlockChain
