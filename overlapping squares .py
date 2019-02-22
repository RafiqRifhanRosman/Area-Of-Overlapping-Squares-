#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:42:04 2019

@author: mdrafiqrifhanrosman
"""
def solution(S, T, U, V, W, X, Y, Z):
    
   
    
    breadth_A = []
    length_A = []
    
    breadth_B = []
    length_B = []
 
#rectangle A
    for i in range (T, (V + 1) ):
        breadth_A.append(i)
        
    sbreadth_A = set()
    for item in breadth_A:
        sbreadth_A.add(item)
    
    
    for j in range (S, (U + 1)):
        length_A.append (j)
        
    slength_A = set()
    for item in length_A:
        slength_A.add(item)
        
    
    
 #rectangle B   
    breadth_B = []
    length_B = []
    
    for i in range (X, (Z + 1) ):
        breadth_B.append(i)
        
    sbreadth_B = set()
    for item in breadth_B:
        sbreadth_B.add(item)
    
    
    for j in range (W, (Y + 1)):
        length_B.append (j)
        
    slength_B = set()
    for item in length_B:
        slength_B.add(item)
        
      
    
    over_len = slength_A.intersection (slength_B)
    
    over_breadth = sbreadth_A.intersection (sbreadth_B)
    
    
    lover_len = list(over_len)
    lover_breadth = list(over_breadth)
    
    l = lover_len[len(lover_len) - 1] - lover_len[0]
        
    b = lover_breadth[len(lover_breadth) - 1] - lover_breadth[0]
        
    Area_A = (V - T) * (U - S)
    Area_B = (Y -W) * (Z-X)
    Area_O = (l * b)
    
    summ = Area_A + Area_B - Area_O
    
    print ("A" ,Area_A) 
    print ("B" , Area_B) 
    print ("O" , Area_O)
    
    
    
    if summ > 2147483647:
        return (-1)
    else:
        return (summ)
   
print (solution (-4, 1, 2, 6, 0, -1, 4, 3))
        
    
    


