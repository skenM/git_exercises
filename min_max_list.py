'''
list = [1,4,-4,7]
list.sort()

print(list)
print("Min in list is:", list[0],"\nMax in this list is:", list[-1])
'''


list = [1,3,7,11,2,-6,10,-13]

min = None
max = None

for i in list:
    if min == None or min > i:
        min = i
    if max == None or max < i:
        max = i
print ("Najmniejsza liczba w liscie to:", min)
print ("Najwieksza liczba w liscie to:", max)
