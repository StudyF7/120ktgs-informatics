k = [1,2,3,4,5,6,7,8,9,10]
l = [1,2,3,4,5,6,7,8,9,10]

for i in range(11):
    k[i] = 10 - i
for i in range(11):
    l[i] = k[6] - k[i]

print(k)
print(l)