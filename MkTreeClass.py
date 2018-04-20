#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:31:25 2018

@author: xingyichong
"""

import pickle
import hashlib


class MerkleTree:
    
    def __init__(self):
        pass

    def Encode_Hash(string):    # to hash the string
        if type(string) != bytes:
            string = string.encode('utf-8')
        return hashlib.sha256(string).hexdigest()  # 256 bit = 2^8
    
    
    def get_root(transactions):    # main function to get the Merkle Tree root
        
        new_transactions = transactions
        if len(transactions) % 2 != 0: 
            new_transactions = (*transactions, '')   #unpack the tuple
        
        tr_list = [pickle.dumps(i) for i in new_transactions]   #return type: bytes
        
        MerkleTree._get_root(tr_list)
         
        return MerkleTree.Encode_Hash(tr_list[0])
    
    
    def _get_root(cur_list):        # recursive function to return the root
        if len(cur_list) == 1: return cur_list
        
        if len(cur_list) % 2 != 0: cur_list.append('')
            
        tr_hash = [MerkleTree.Encode_Hash(i) for i in cur_list]
        
        tr_new = []
        for i in range(0, len(cur_list)-1, 2):
            tr_new.append(tr_hash[i] + tr_hash[i+1])
        
        MerkleTree._get_root(tr_new)
