'''
list = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]
print(list)

set = {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10}
print(set)
'''










'''
set1 = {1,2}
print(type(set))
set1.add(9)
print(set1)

for element in set1:
    print(element)
    print("😂")
'''

'''
set1 = {1,2,3,4,4,5,6,7,8,8,9}
set2 = {10,10,11,12,14,14,15,16,16}
'''
'''
for element in set2:
    set1.add(element)
print(set1)
set1.update(set2)
print(set1)
'''
'''
for element in set2:
    set1.add(element)
print(set1)
'''
'''
set1.remove(2)
print(set1)
set1.discard(3)
print(set1)
set1.pop()
print(set1)
'''
'''
set1 = {1,3,5,7,9,11,2,4,6,8,10}
for element in set1:
    if(element % 2 == 0):
        set1.remove(element)
print(set1)

'''
#Assignment 1
# Discard chosen
'''
set = {1,2,3,4,4,4,4,5,6,7,8,9,10}
for element in set:
    if(element == 4):
        set.discard(element)
print(element)
print(set)
'''

'''


index = 0
list = [1,3,5,7,9,8,6,4,2,4,8]
while index < len(list):
    if(list[index] % 2 == 0):
        list.remove()
print(list)
'''
'''
list = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for element in list:
    if (element % 2 == 0):
        list2.append(element)
        list2.sort(reverse = True)
print(list2)
'''
'''
oldset = {1,2,3,4,4,4,4,5,6,7,8,9,10}
oldset = {b for b in oldset if b % 2 != 0}
print(oldset)
'''






