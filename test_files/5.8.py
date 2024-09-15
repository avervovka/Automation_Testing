a, b = list(map(float, input().split())), list(map(float, input().split()))
c = [int(a[i] + b[i]) for i in range(len(a))]
print(*c)