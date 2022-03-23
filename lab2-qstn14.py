A = set()
n = int(input("Enter the limit of the set : "))
print("Enter the elements of the set\n")
for i in range (n):
    k = int(input(''))
    A.add(k)
print("The set you have entered is ",A)
item = int(input("Enter the item to be removed : "))
if item in A:
    A.remove(item)
    print("Item removed")
else:
    print("The item is not removed. The item may not be in the set.")

print("The final set is ",A)