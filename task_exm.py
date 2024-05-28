# a, s, p = 1, 150, 200
#
# while a <= 10:
#     a += 2
#     p += a
#     s += p
#
# print(s)
# print('end')

# S = 1
# N = 0
# for i in range(6):
#     N+=1
#     S = S * N
# print(S)
# print('end')

m = 12
n = 5
while m != n:
    if m > n:
        m = m - 2 * n
    else:
        n = n - 3

print(f'm: {m}, n: {n}')
print('end')
# задача 4
k, l = [], []

for i in range(1, 11):
    k.append(10 - i)
for i in range(11):
    l.append(k[5] - k[i - 1])
print(k)
print(l)