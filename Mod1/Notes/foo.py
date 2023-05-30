def foo2(n):  
    print("n= ", n) 
    sum = 0
    for i in range(n):
        # print("i = ", i)
        for j in range(n):
            # print("j = ", j)
            if( i == j):
                print("inner loop iteration (j, i): ", j, i)
                for k in range(n*n):
                    sum = i + j + k
                    print("k = ", k)
                    print()




foo2(3)
