# -*- coding: utf-8 -*-

import sys

count=0

input = sys.stdin.read()

with open('input.txt') as f:
    input = f.readlines()
    input = map(str.split, input)
    input = [list(map(int, x)) for x in input]
    
input.pop(0)

for i in input:
    count+=1
    result='good'
    for j in range(0, len(i)):
        if i[j] > 20:
            result='bad'
            break
    print('Case %s: %s' % (count, result))
            
    