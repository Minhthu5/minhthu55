# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:51:40 2024

@author: 
"""
import math 
a = float(input("Nhap so thuc a:"))
b = float(input("Nhap so thuc b:"))
a=math.sqrt(a)
aa=math.sqrt(math.sqrt(a))
ab=math.sqrt(math.sqrt(a*b))
b=math.sqrt(b)
bb=math.sqrt(math.sqrt(b))
x = ((a-b)/(aa-bb)) - ((a+ab)/(aa+bb))
print(f"Gia tri cua bieu thuc la: {x}")
