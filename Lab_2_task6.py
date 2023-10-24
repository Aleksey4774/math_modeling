"""for i in range(0, 9, 1):
     print(i + 1, end = " ")  
for a in range(2, 10, 1):
        print(a + 1, end="\n") 
        for i in range(1, 10, 1):
            print(i * a , end = " ")"""





for i in range(1,10,1):
    for j in range(1,10,1):
        print((j * i), end = " ")
        if j == 9:
           print( )