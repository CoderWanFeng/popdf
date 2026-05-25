# for 循环示例（已有的）
num_list = [1, 2, 3, 4, 5]
for num in num_list:
    print(num)

print(num_list)

stu={
    "name":"晚枫",
    "age":18,
    "gender":"男"
}

for key,value in stu.items():
    print(key,value)

# ==================== 集合遍历示例 ====================
print("\n=== 集合遍历示例 ===")

# 1. 创建一个集合
fruits = {"苹果", "香蕉", "橙子", "葡萄", "苹果"}  # 注意：重复的"苹果"会被自动去重
print(f"集合内容: {fruits}")
print(f"集合长度: {len(fruits)}")

# 2. 使用 for 循环遍历集合
print("\n使用 for 循环遍历集合:")
for fruit in fruits:
    print(f"水果: {fruit}")

# 3. 集合的其他操作示例
print("\n集合的其他操作:")

# 添加元素
fruits.add("西瓜")
print(f"添加西瓜后: {fruits}")

# 删除元素
fruits.remove("香蕉")
print(f"删除香蕉后: {fruits}")

# 遍历修改后的集合
print("\n遍历修改后的集合:")
for fruit in fruits:
    print(f"水果: {fruit}")

# 4. 数字集合的遍历
print("\n数字集合的遍历:")
numbers = {1, 2, 3, 4, 5, 3, 2}  # 重复元素会被自动去重
for num in numbers:
    print(f"数字: {num}")
