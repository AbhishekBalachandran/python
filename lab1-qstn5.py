from stringprep import b1_set


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a_set = set(a)
b_set = set(b)
if(a_set & b_set):
    print("The common numbers are : ",a_set&b_set)
else:
    print("no common elements.")