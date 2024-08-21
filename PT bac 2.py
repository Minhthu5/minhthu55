# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:48:28 2024

@author: MinhThu
"""

import math
a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))
print("{0}x^2 + {1}x + {2} = 0".format(a,b,c))
if a!=0:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("phương trình vô nghiệm")
    elif delta ==0:
        x = -b/2*a
        print("phương trình có nghiệm kép x1 = x2 = ",x)
    else:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("phương trình có 2 nghiệm phân biệt x1 = {0} và x2 = {1}".format(x1,x2))
else:
    print("không phải phương trình bậc 2")
    
