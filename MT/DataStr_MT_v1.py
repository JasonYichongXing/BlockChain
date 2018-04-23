#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:28:27 2018

@author: xingyichong
"""
import math

HANDLE_MISSING = ''  #  define the way to handle the node without right child.

class Tree:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.leftTree = left
        self.rightTree = right
    
    def __str__(self):
        if self.leftTree == None or self.rightTree == None:
            return '\nThis node is leaf: ' + str(self.value)
        return '\nThis node is: ' + str(self.value) + '\nLeft Child is: ' + str(self.leftTree.value) + '\nRight Child is: ' + str(self.rightTree.value)

def _nextlvl(cur_level):   
    # return the length of the parent level.
    if type(cur_level) != int:
        raise ValueError('The level# must be an integer!')
    return math.ceil(cur_level/2)

def _get_Hierarchy(mystring):
    # return a int list containing the tree hierarchy. 
    lvl_list = [len(mystring)]
    i = 1
    while lvl_list[-1]>1:
        lvl_list.append(_nextlvl(lvl_list[i-1]))
        i += 1
    return lvl_list
    
def Build_Tree(mystring):
    # the main function to build a tree without hashing.
    Tree_dict = dict([
        ((1,i),Tree(mystring[i])) for i in range(len(mystring))]).  # Dumping in the leaf info.

    height = math.ceil(math.log(len(mystring),2)) + 1
    Tree_hierarchy = _get_Hierarchy(mystring)
           
    for i in range(2, height+1):   # i is the index of level.
        for j in range(Tree_hierarchy[i-1]):    # j is the index of node in current level.
            
            Left_value = Tree_dict[i-1,j*2].value
            right_child = None 
            
            try:
                Right_value = Tree_dict[i-1,j*2+1].value
                right_child = Tree_dict[i-1,j*2+1] 

            except: 
                Right_value = HANDLE_MISSING
                
            Tree_dict[(i,j)] = Tree(Left_value+Right_value, Tree_dict[i-1,j*2], right_child)
    return Tree_dict



###################
# Test:

def main(mystring):
    TreeDict = Build_Tree(mystring)
    for i in TreeDict:
        print(i,':', TreeDict[i])
        
if __name__ == "__main__":
    x = 'dsawsdw1jcmsetkspbx['
    main(x)   
