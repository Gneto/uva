# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:05:49 2017

@author: 
"""

input = open('salary.txt')
input = map(str.split, input)
input = [list(map(int, x)) for x in input]

count=0

input.pop(0)

for i in input:
    count+=1
    i.sort()
    print('Case %s: %s' % (count, i[1]))
