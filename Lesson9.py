#1
print("Введите количество чисел:")
n = int(input())

print("Введите числа через пробел:")

strch = input().split()

mnozh = set(strch)

print("количество различных чисел: " + str(len(mnozh)))

#2
print("Введите первый список чисел через пробел:")

sp1 = input().split()

print("Введите второй список чисел через пробел:")

sp2 = input().split()

print("количество чисел в 2-х списках: " + str(len(sp1) + len(sp2)))


#3
print("Введите список чисел через пробел:")

sp = input().split()

mn = set()
for el in sp:
    if el in mn:
        print("YES")
    else:
         print("NO")  
         mn.add(el)
