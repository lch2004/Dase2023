import math

task = ""
a = float(input())
b = math.modf(a)
c = b[0]
task +=str(int(b[1]))
task +="."
while c > 0 :
    c *= 2
    task += str(int(c))
    c -= int(c)
print(task)