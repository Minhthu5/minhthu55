# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:12:44 2024

@author: MinhThu
"""
a = int(input("Nhập số nguyên thứ nhất (a): "))
b = int(input("Nhập số nguyên thứ hai (b): "))
tong = a + b
hieu = a - b
tich = a * b
if b != 0:
    thuong = a / b
    chia_liu = a % b
    chia_nguyen = a // b
    thuong_2_chu_so = round(thuong, 2)
    thuong_3_chu_so = round(thuong, 3)
else:
    thuong_2_chu_so = thuong_3_chu_so = "Không xác định (chia cho 0)"
    chia_liu = chia_nguyen = "Không xác định (chia cho 0)"
print("Tổng của a và b là:", tong)
print("Hiệu của a và b là:", hieu)
print("Tích của a và b là:", tich)
print("Thương của a và b (làm tròn 2 chữ số):", thuong_2_chu_so)
print("Thương của a và b (làm tròn 3 chữ số):", thuong_3_chu_so)
print("Chia lấy dư của a và b là:", chia_liu)
print("Chia lấy nguyên của a và b là:", chia_nguyen)
