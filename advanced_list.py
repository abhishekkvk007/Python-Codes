first=[1,2,3,4,5]
second=[6,7,8,9,10]
third=first+second
print(third)
first.extend(second)
print(first)
print(second)






remove_list=[1,2,3,4,5,"Hello"]
print(remove_list)
remove_list.remove(1)
print(remove_list)
remove_list.remove(2)
print(remove_list)
remove_list.pop(0)
print(remove_list)
remove_list.pop()
print(remove_list)
del remove_list[0]
print(remove_list)
del remove_list
print(remove_list)



for_list=[1,2,3,4,5,6,7,8,9,10]
for x in for_list:
    print(x)