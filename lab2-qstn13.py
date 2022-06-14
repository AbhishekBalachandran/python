from itertools import count


list = [[1,4],['one',2,3,'four'],[2,3],4,[5,6,7]]
count = 0
for i in list:
    if len(i) > 1:
        count += 1
        print(count,". sublist of list : ",i)
    else:
        continue
        