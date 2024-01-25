#蒙特卡罗
import  random
n = 100000
i = 0.0
for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x ** 2 + y ** 2
    if distance <= 1:
           i += 1
print(i / 25000)

#级数
i = 0
pai = 0
for i in range(n):
    pai += (-1)**i /(2*i+1)
print(4*pai)


import math
import  random
n = 100000
i1 = i2 =0
for _ in range(n):
    x1 = random.uniform(2,3)
    y1 = random.uniform(0,9)
    y2 = random.uniform(0,12)
    if y1 - x1**2 <= 0:
           i1 += 1
    if y2 - 4*x1*math.sin(x1) <=0:
           i2 += 1
print((i1 * 9+i2 * 12)/n)
print(19/3+(2*math.cos(2)-3*math.cos(3)+math.sin(3)-math.sin(2))*4)