﻿#Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.
print('введите количество чисел')
quant=int(input())
zeros=0
print('введите числа через enter')
while(quant > 0):
    num=int(input())
    if num==0:
        zeros+=1
    quant-=1    
print("количество нулей",zeros)