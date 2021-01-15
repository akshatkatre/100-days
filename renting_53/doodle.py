l1 = [i for i in range(0, 10)]
l2 = ["a"+ str(i) for i in range(10, 20)]
data = {}
for i in range(len(l1)):
    data[i] = {'val': l1[i],
               'address': l2[i]}

print(data)