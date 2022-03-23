dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
concatenated_dic = dic1.copy()
concatenated_dic.update(dic2)
concatenated_dic.update(dic3)
print(concatenated_dic)