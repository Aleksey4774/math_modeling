a = int(input("Введите первый член: "))
b = int(input("Введите знаменатель прогрессии: "))
c = int(input("Введите количество членов: "))

chisl = a*((b**c)-1)
znam = b - 1
otv = chisl / znam

print(otv)