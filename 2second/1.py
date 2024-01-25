def maxa(n):
    dp = [0] * (n + 1)
    result = [[] for _ in range(n + 1)]
    dp[1] = 1
    result[1] = [1]
    for i in range(2, n + 1):
        max_b = 0
        max_c = 0
        for j in range(1, i // 2 + 1):
            current_b = dp[j] * dp[i - j]
            if current_b > max_b:
                max_b = current_b
                max_c = c
        if max_b > i:
            dp[i] = max_b
            result[i] = result[max_c] + result[i - max_c]
        else:
            dp[i] = i
            result[i] = [i]
    return result[n]

n = 9
result_list = maxa(n)
print("正整数列表:", result_list)