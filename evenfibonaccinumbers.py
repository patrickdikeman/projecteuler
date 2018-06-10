l = [1,2]
list = []
for i in l:
    if i < 4000000:
        l.append(l[-1]+l[-2])
for i in l:
    if i % 2 == 0:
        list.append(i)
list_sum = sum(list)
print (list_sum)
