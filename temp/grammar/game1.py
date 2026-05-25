
# 示例列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始列表: {numbers}")

# 方法1：使用 for 循环
print("\n方法1：使用 for 循环:")
for num in numbers:
    if num % 2 == 0:
        print(f"{num} 是偶数")
    elif num % 2 != 0:
        print(f"{num} 是奇数")
    else:
        print(f"{num} 不是偶数也不是奇数")
# 方法2：使用 while 循环
print("\n方法2：使用 while 循环:")
index = 0
while index < len(numbers):
    num = numbers[index]
    if num % 2 == 0:
        print(f"{num} 是偶数")
    else:
        print(f"{num} 是奇数")
    index += 1

# 方法3：创建新列表，只包含偶数
print("\n方法3：创建新列表，只包含偶数:")
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"偶数列表: {even_numbers}")
