﻿#Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)
print('введите число')
num=int(input())
cand=num
#сразу включаем вариант "само на себя"
dels=1
while(cand>1):
    if num%cand==0:
        dels+=1   
    cand-=1
print("количество делителей равно", dels)
        

