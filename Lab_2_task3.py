year = int(input("Введите год: "))
if year % 400 == 0:
    print("Год високосный ")
elif year % 100 != 0 and year % 4 == 0:
    print("Год высокосный")
else:    
    print("Год не високосный  ")  
