#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:43:13 2017

@author: orlando
"""

def recursion(field):
    global i
    aux = len(str(field))
    if aux == field:
        print(i)
    else:
        field = aux
        i += 1
        recursion(field)

while True:
    field=input().strip()
    if field == 'END':
        break
    elif field == '1':
        print(1)
        continue
    i = 1
    recursion(field)