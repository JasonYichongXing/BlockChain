#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:53:54 2018

@author: xingyichong
"""
import math
import hashlib

class MerkleTree:

    def __init__(self, Tx_info = None):
        self.tx_info = Tx_info
        self.sizeLeaf = len(Tx_info)
        
    def Calc_Height(self):
        return math.ceil(math.log(self.sizeLeaf, 2)) + 1
    
    def Get_Hierarchy(self):
        listHrcy = []        
        sizetoinsert = self.sizeLeaf
        while sizetoinsert > 1:
            listHrcy.append(sizetoinsert)
            sizetoinsert = math.ceil(sizetoinsert / 2)
        
        listHrcy.append(1)
        return listHrcy[::-1]
    
    def HashofLeaf(self):
        return [Encode_Hash(i) for i in self.tx_info]

    def Get_Root(self):
        return self.BuildEntireTree()[-1]
    
    
    def BuildEntireTree(self):
        newHashlist = curHashlist = self.HashofLeaf()

        while len(newHashlist) != 1:
            newHashlist = self._BuildEntireTree(newHashlist)
            curHashlist.extend(newHashlist)
            
        return curHashlist
        

    def _BuildEntireTree(self,curLevel):
        list_Hashed_Tree = []

        for i in range(0, len(curLevel)-1, 2):
            c1 = curLevel[i]
            c2 = curLevel[i+1]
            list_Hashed_Tree.append(self.BuildParentNode(c1, c2))
        
        if len(curLevel) % 2 != 0:
            c1 = curLevel[-1]
            c2 = None
            list_Hashed_Tree.append(self.BuildParentNode(c1, c2))

        return list_Hashed_Tree
    
   
    def BuildParentNode(self, ChildNode1, ChildNode2):
        if ChildNode2 == None:
            ParentNode = ChildNode1
        else:
            ParentNode = Encode_Hash(ChildNode1 + ChildNode2)
        return ParentNode


def Encode_Hash(stringInfo):    # to hash the string
        if type(stringInfo) != bytes:
            stringInfo = stringInfo.encode('utf-8')
        return hashlib.sha256(stringInfo).hexdigest()
