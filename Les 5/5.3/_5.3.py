﻿#Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно. 
#У Майкла A долларов, у Ивана B долларов. 
#Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan,
#если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
print('Введите минимальную сумму инвестиций')
fund=int(input())
print('Введите средства Майкла')
Mike=int(input())
print('Введите средства Ивана')
Ivan=int(input())
#Проверка индивидуальной возможности.
if Mike>=fund and Ivan>=fund:
    print('2')
elif Mike>=fund or Ivan>=fund:
    if Mike>=fund:
        print('Mike')
    else:
        print('Ivan')
#проверка коллективной возможности.
else:
    if (Mike+Ivan)>=fund:
        print('1')
    else:
        print('0')