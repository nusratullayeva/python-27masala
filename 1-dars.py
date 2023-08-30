# 1-masala
# nameInput = input('Ismingizni kiriting: ')
# surnameInput = input('Familiyangizni kiriting: ')
# yearInput = int(input('Yilingizni kiriting: '))
# print(f'Mening ismim {nameInput}, familiyam {surnameInput}, yoshim {2023 - yearInput} da!')



# 2-masala
# inputNum = int(input('Kiriting: '))
# inputNum2 = inputNum**2
# print(inputNum2)



# 3-masala
# inputNum3 = int(input('a ni Kiriting: '))
# inputNum4 = int(input('b ni Kiriting: '))
# resultInputs = inputNum3 * inputNum4
# resultInputs2 = 2 * (resultInputs)
# print(resultInputs2)



# 4-masala
# inputNum = int(input('Kiriting: '))
# inputNum2 = inputNum * 3.14
# print(inputNum2)



# 5-masala
# a = float(input("Kubning yon tomonini kiriting: "))
# V = a ** 3
# S = 6 * a ** 2
# print(f"Kubning hajmi {V} ga, to'la sirti esa {S} ga teng.")



# 6-masala
# def parallelepiped(a, b, c):
#     V = a * b * c
#     S = 2 * (a * b + b * c + a * c)
#     return V, S
# V, S = parallelepiped(7, 8, 9)
# print("Paralelepipedning hajmi:", V)
# print("Paralelepipedning to'la sirti:", S)



# 7-masala
# import math
# R = float(input("Doiraning radiusini kiriting: "))
# L = 2 * math.pi * R
# S = math.pi * R ** 2
# print(f"Doira uzunligi: {L:.2f}")
# print(f"Doira yuzasi: {S:.2f}")



# 8-masala
# Ainput = int(input('Birinchi sonni kiriting: '))
# Binput = int(input('Ikkinchi sonni kiriting: '))
# resultInputs =(Ainput + Binput) / 2
# print(resultInputs)



 # 10-masala
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# yigindi = a + b
# kopaytma = a * b
# birinchi_kvadrat = a ** 2
# ikki_kvadrat = b ** 2
# print(f"Ularning yig'indisi: {yigindi}")
# print(f"Ularning ko'paytmasi: {kopaytma}")
# print(f"Birinchi sonning kvadrati: {birinchi_kvadrat}")
# print(f"Ikkinchi sonning kvadrati: {ikki_kvadrat}")



# 11-masala
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# yigindi = a + b
# kopaytma = a * b
# birinchi_modul = abs(a)
# ikki_modul = abs(b)
# print(f"Ularning yig'indisi: {yigindi}")
# print(f"Ularning ko'paytmasi: {kopaytma}")
# print(f"Birinchi sonning moduli: {birinchi_modul}")
# print(f"Ikkinchi sonning moduli: {ikki_modul}")



# 13-masala
# import math
# R1 = float(input("R1 ni kiriting: "))
# R2 = float(input("R2 ni kiriting: "))
# S1 = math.pi * R1 ** 2
# S2 = math.pi * R2 ** 2
# S3 = S1 - S2
# print(f"S1 = {S1}")
# print(f"S2 = {S2}")
# print(f"S3 = {S3}")



# 14-masala
# import math
# L = float(input("Aylana uzunligini kiriting: "))
# R = L / (2 * math.pi)
# S = math.pi * R ** 2
# print(f"Aylananing radiusi: {R}")
# print(f"Aylananing yuzasi: {S}")



# 15-masala
# import math
# S = float(input('Aylana yuzasini kiriting: '))
# R = math.sqrt(S / math.pi)
# D = 2 * R
# print(f"Radius: {R:.2f}")
# print(f"Diametr: {D:.2f}")



# 16-masala
# import math
# x1 = float(input('X1 sonni kiriting: '))
# y1 = float(input('Y1 sonni kiriting: '))
# x2 = float(input('X2 sonni kiriting: '))
# y2 = float(input('Y2 sonni kiriting: '))
# d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print(f"Masofa: {d:.2f}")



# 17-masala
# import math
# A = (1, 2)
# B = (5, 6)
# C = (3, 4)
# AC = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2)
# BC = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2)
# total_length = AC + BC
# print(f"AC: {AC:.2f}")
# print(f"BC: {BC:.2f}")
# print(f"Kesmalar uzunligining yig'indisi: {total_length:.2f}")



# 18-masala
# import math
# A = (1, 2)
# B = (5, 6)
# C = (3, 4)
# AC = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2)
# BC = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2)
# product = AC * BC
# print(f"AC: {AC:.2f}")
# print(f"BC: {BC:.2f}")
# print(f"Kesmalar uzunligining ko'paytmasi: {product:.2f}")



# 19-masala
# x1, y1 = 0, 0
# x2, y2 = 3, 0
# x3, y3 = 3, 4
# x4, y4 = 0, 4
# d1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# d2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
# d3 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5
# d4 = ((x1 - x4) ** 2 + (y1 - y4) ** 2) ** 0.5
# perimeter = d1 + d2 + d3 + d4
# area = abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1) - (y1 * x2 + y2 * x3 + y3 * x4 + y4 * x1)) / 2
# print(f"To'g'ri to'rtburchakning perimetri: {perimeter}")
# print(f"To'g'ri to'rtburchakning yuzasi: {area}")



# 22-masala
# A = input('A Son kiriting: ')
# B = input('B Son kiriting: ')
# A, B = B, A
# print(f"A ning yangi qiymati: {A}")
# print(f"B ning yangi qiymati: {B}")



# 23-masala
# A = int(input('A son kiriting: '))
# B = int(input('B son kiriting: '))
# C = int(input('C son kiriting: '))
# print(f'A teng {B} ga')
# print(f'B teng {C} ga')
# print(f'C teng {A} ga')



# 24-masala
# A = int(input('A son kiriting: '))
# B = int(input('B son kiriting: '))
# C = int(input('C son kiriting: '))
# print(f'A teng {C} ga')
# print(f'B teng {A} ga')
# print(f'C teng {B} ga')



# 25-masala
# def y(x):
#     return 3 * x ** 6 - 6 * x ** 2 - 7
# x = 5
# print(f"y({x}) = {y(x)}")



# 26-masala
# def my_function(x):
#     y = 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2
#     return y
# x = float(input("x ning qiymatini kiriting: "))
# print(f"funksiya qiymati {my_function(x)}")



# 27-masala
# def my_function(a):
#     if a == 0:
#         return "Daraja 0 ga teng"
#     elif a == 1:
#         return "Daraja 1 ga teng"
#     else:
#         i = 1
#         while i <= a:
#             if i * i == a:
#                 return f"Daraja {i} ga teng"
#             elif i * i > a:
#                 return f"{i - 1} ning kvadrati"
#             else:
#                 i += 1
# a = int(input("A ning qiymatini kiriting: "))
# print(f"{my_function(a)}")



# 28-masala
# def daraja_hisobla(A):
#     return [A**2, A**3, A**5, A**10, A**15]
# A = int(input("A ni kiriting: "))
# darajalar = daraja_hisobla(A)
# print(f"A ning darajalari: {darajalar}")



# 33-masala
# def konfet_turishini_aniklovchi(X, A):
#     return X // A
# X = int(input("X ni kiriting: "))
# A = int(input("1 kilogramm konfet narxini kiriting: "))
# konfet_soni = konfet_turishini_aniklovchi(X, A)
# print(f"{X} kilogramm konfet {konfet_soni} ta {A} so'mlik konfetga teng keladi.")



# 34-masala
# def narx_hisobla(A, B):
#     return A / B
# X = int(input("X ni kiriting: "))
# A = int(input("1 kilogramm shokolad narxini kiriting: "))
# Y = int(input("Y ni kiriting: "))
# B = int(input("1 kilogramm konfet narxini kiriting: "))
# shokolad_narxi = narx_hisobla(A, 1)
# konfet_narxi = narx_hisobla(B, 1)
# print(f"1 kg shokolad {shokolad_narxi} so'mga, 1 kg konfet {konfet_narxi} so'mga turadi.")



# 38-masala
# def chiziqli_tenglama_yechimi(A, B):
#     return -B / A
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# x = chiziqli_tenglama_yechimi(A, B)
# print(f"Chiziqli tenglama {A}*x + {B} = 0 ning yechimi x = {x} ga teng.")
