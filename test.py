number = [1,2]
text=["ad","sdf"]
abc=[]
length =len(number)
for i in range(0, length):
    abc.append(text[i]*int(number[i]))
print(abc)