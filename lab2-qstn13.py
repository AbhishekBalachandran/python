def displaysublist(A):
    B = []
    for i in range(len(A)+1):
        for j in range (i+1,len(A)+1):
            sub = A[i:j]
            B.append(sub)
    return B

A = list()
n =int(input("Enter the size of the list : "))
print("Enter the elements of the list \n")
for i in range(int(n)):
    k = int(input(''))
    A.append(k)
print("Given list is ",A)
print("Sublist is ",displaysublist(A))

