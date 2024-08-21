# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:28:22 2024

@author: MinhThu
"""
N = int(input("Nhập số nguyên dương có 2 chữ số (N): "))
if 10 <= N <= 99:
    chuc = N // 10   
    donvi = N % 10   
    tong = chuc + donvi
    print(f"{chuc} + {donvi} = {tong}")
else:
    print("Số nhập vào không phải là số nguyên dương có 2 chữ số.")
