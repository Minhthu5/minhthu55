# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:32:08 2024

@author: MinhThu
"""
gio = int(input("Nhập giờ (0-23): "))
phut = int(input("Nhập phút (0-59): "))
giay = int(input("Nhập giây (0-59): "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    tong_giay = gio * 3600 + phut * 60 + giay
    print(f"Tổng số giây là: {tong_giay}")
else:
    print("Giá trị nhập vào không hợp lệ. Hãy kiểm tra lại giờ, phút và giây.")