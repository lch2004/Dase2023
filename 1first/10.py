a = input()
a = list(a)
b = 0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        b = 1
        break
print(b)