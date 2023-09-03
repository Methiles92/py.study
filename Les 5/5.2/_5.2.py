#Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
#Для решения задачи создайте переменную и в неё положите слово с помощью input()
#А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False


print("Введите слово")
word=str(input())
l=list(word)
sogl=0
gli=0
glo=0
glu=0
gle=0
gla=0
i=0
while i<len(l):
    if l[i]!="a" and l[i]!="i" and l[i]!="o" and l[i]!="e" and l[i]!="u":
        sogl+=1 
    else:
        if l[i]=="i":
            gli+=1
        elif  l[i]=="a":
            gla+=1
        elif  l[i]=="e":
            gle+=1
        elif  l[i]=="o":
            glo+=1
        else:
            glu+=1
    i+=1
glas=gla+glo+glu+gli+gle
print("Всего согласных", sogl)
print("Всего гласных", glas)
def check(x):
    if x==0:
        return "False"
    else:
        return x
print("букв a =", check(gla))
print("букв i =", check(gli))
print("букв u =", check(glu))
print("букв e =", check(gle))
print("букв o =", check(glo))
