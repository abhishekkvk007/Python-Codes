num=12345
sum=0
for i in range(len(str(num))):
    temp=num%10
    num=num//10
    print(num)
    sum+=temp
print(sum)
#



