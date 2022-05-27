# 开发者 haotian
# 开发时间: 2022/5/21 20:24
'''
accept function as parameter or let the function as the back
'''


def fact(n):
    return n**2


l = [fact(n) for n in range(12) if n & 1 == 0]

print(l)

