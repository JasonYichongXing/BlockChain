#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:34:48 2018

@author: xingyichong
"""
#https://blockchain.info/block/00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048

import pickle
import hashlib


def Encode_Hash(string):    # to hash the string
    if not isinstance(string, bytes):
        string = string.encode('utf-8')
    return hashlib.sha256(string).hexdigest()


def get_root(transactions):    # main function to get the Merkle Tree root
    if len(transactions) % 2 != 0: transactions.append('')
    
    tr_list = [pickle.dumps(i) for i in transactions]   #return type: bytes
    
    _get_root(tr_list)
     
    return Encode_Hash(tr_list[0])


def _get_root(cur_list):        # recursive function to return the root
    if len(cur_list) == 1: return cur_list
    
    if len(cur_list) % 2 != 0: cur_list.append('')
        
    tr_hash = [Encode_Hash(i) for i in cur_list]
    
    tr_new = []
    for i in range(0, len(cur_list)-1, 2):
        tr_new.append(tr_hash[i] + tr_hash[i+1])
    print(tr_new, '\n==========')
    
    _get_root(tr_new)

    
#######################
#Test
            
Transaction = [
        {'Pay':'A1', 'Rec': 'B1', 'Amt': 100}, 
        {'Pay':'A2', 'Rec': 'B2', 'Amt': 300}, 
        {'Pay':'A3', 'Rec': 'B3', 'Amt': 50},
        {'Pay':'A4', 'Rec': 'B3', 'Amt': 10},
        {'Pay':'A2', 'Rec': 'B6', 'Amt': 20},
        {'Pay':'A2', 'Rec': 'B6', 'Amt': 30},
        {'Pay':'A2', 'Rec': 'B6', 'Amt': 40},
        {'Pay':'A2', 'Rec': 'B6', 'Amt': 50},
        {'Pay':'A2', 'Rec': 'B6', 'Amt': 9},
        ]



root = get_root(Transaction)
assert len(root) == 64

print('Merkle Root: ', root)
