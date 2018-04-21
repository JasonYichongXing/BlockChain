#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 00:17:14 2018

@author: xingyichong
"""

'''Test for BlockChain '''

import JasonBTC

def Test_func(N = 20):
    
    print('\Below, a BlockChain with %s Blocks(Diff = %s):' % (N,JasonBTC.INIT_DIFFICULTY))
    Example = JasonBTC.Generate_BlockChain(N)

    for _ in Example:
        print(_.BlockNo, ': ', _.Hash)

    for _ in Example:
        print(_)

if __name__ == "__main__":
    Test_func()
