list1=['a','b','c']
list2=['d','e','f']
list3=['g','h','i']
list4=list1
list4.append('100')
print(list1)

list5=list1.copy()
list5.append('200')
print(list5)
print(list1)


tuple=(0,1,2,3,4,5,6,7,8,9)
len=len(tuple)
print(len)

print(tuple[:len])
print(tuple[3:6])
print(tuple[6:9])
print(tuple.count(5))
print(tuple.index(1))

fruits=("apple","banana","cherry","guava","mango","pineapple")
a,b,*c=fruits
print(a)
print(b)
print(c)


ttuple=(1,2,3,4)
ttuple=list(ttuple)
ttuple.append(ttuple)
ttuple=tuple(ttuple)
print(ttuple)



set={1,2,3,4,5,5}
print(set)
