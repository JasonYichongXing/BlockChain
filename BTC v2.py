#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:12:32 2018

@author: xingyichong
"""

import hashlib
import datetime

from MkTreeClass import MerkleTree as MK


INIT_DIFFICULTY = 2
MAX_NONCE = 2**32

INIT_BlOCKNO = 0
INIT_INFO = None
INIT_NNONCE = 0
INIT_PREV_HASH = 0
INIT_TIMESTAMP = datetime.datetime(2018, 6, 19)
INIT_GENESIS = 'First Block. ' + str(INIT_TIMESTAMP)

class Block:
    def __init__(self, Transaction_info=INIT_INFO):
        self.BlockNo = INIT_BlOCKNO
        self.nTime = INIT_TIMESTAMP
        self.previous_hash = INIT_PREV_HASH
        self.Nonce = INIT_NNONCE
        self.Info = Transaction_info
        self.next = None
        
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
        return '\nBlock No: ' + str(self.BlockNo) + \
               '\nBlock Hash: ' + str(self.Hash) + \
               '\nPrevius Hash: ' + str(self.previous_hash) + \
               '\nMerkleRoot: ' + str(self.MerkleRoot) + \
               '\nNonce: ' + str(self.Nonce) + \
               '\nTransaction Info: ' + str(self.Info) + \
               '\n============\n'


class Blockchain:
    def __init__(self, geninfo=INIT_GENESIS):
         self.genesis = Block(('Genesis', INIT_GENESIS))
         
    @property
    def length(self):
        l = 0
        currentblock = self.genesis
        while currentblock:
            l += 1
            currentblock = currentblock.next
        return l
        
    @property
    def tail(self):
        return self._loopthru(-1)
        
    def addnewblock(self, newinfo):
        
        newblock = Block(newinfo)
    
        newblock.BlockNo = self.tail.BlockNo + 1
        newblock.previous_hash = self.tail.Hash
        while not isPoW(newblock) and newblock.Nonce < MAX_NONCE:
            newblock.Nonce += 1            
        self.tail.next = newblock


    def _loopthru(self, n):
        if n < 0:
            n = self.length + n
        if n > self.length - 1 or n < 0:
            raise IndexError

        currentblock = self.genesis
        while currentblock.BlockNo < n:
            currentblock = currentblock.next
        return currentblock
        

    def __getitem__(self, n):
        return self._loopthru(n).Info
    
    def __iter__(self):
        currentblock = self.genesis
        while currentblock:
            yield currentblock
            currentblock = currentblock.next    
    
    def __len__(self):
        return self.length

    
def isPoW(block, Diff=INIT_DIFFICULTY):
    """ return the hash once Prove_of_Work is confirmed under current difficulty."""
    Diff_string = ''.join('0' for _ in range(Diff))
    return block.Hash[:Diff] == Diff_string
