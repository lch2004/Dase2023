#就思路上
import time

# 开始时间
start_time = time.time()

# 执行需要计时的代码

for _ in range(1000000):
    _ = 2 * 2

# 结束时间
end_time = time.time()

#相减计算执行时间
execution_time = end_time - start_time

print(f"程序执行时间：{execution_time} ")