dict={1:"You",2:"Me",3:"Me"}
dict.update({4:"She"})
print(dict)
dict["5"]="I"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()
print(dict)
del dict[2]
print(dict)
dict.clear()
print(dict)