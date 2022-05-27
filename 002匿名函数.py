# 开发者 haotian
# 开发时间: 2022/5/21 21:11
'''
lambda
'''

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'banana']
f = lambda word: word[::-1]
print(f(fruits))
print(sorted(fruits, key=lambda word: word[::-1]))