A = [1,3,5,2,11,7]
print ("Podaje sume liczb:")
suma = input()

for i in A:
    if i + (i+1) == suma:
        print ("jest suma")
    elif i + (i+1) != suma:
        print (i+1)
        print (i)






'''
s = 0
x = input()
while x>0:
    s += x
    x = input()
print (s)
'''