for i in range(2, 1001):
    for j in range(2, i//2):
        if (i % j) == 0: 
           break
    else: 
       print(i)
