import itertools
s = "aeiou"
t = list(itertools.permutations(s,len(s)))
for i in range(0,len(t)):
    print(t[i])
