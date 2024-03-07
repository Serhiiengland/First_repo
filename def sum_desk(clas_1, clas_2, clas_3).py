#Шоколадка має розмір n на m долек.
#З'ясуйте чи можна один разломом відділити частину, 
#яка містить k долек.

n, m = 3, 5
k = int(input("enter k>>>"))
if k >= n * m:
    print ("|You can't do it")
elif k % n == 0 or k % m == 0:
    print("You can do it")
else:
    print("You can't do it")


 