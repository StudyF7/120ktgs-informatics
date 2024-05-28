m = 12
n = 5
while m != n:
    if m > n:
        m = m - 2 * n
    else:
        n = n - 3

print(f'm: {m}, n: {n}')
print('end')