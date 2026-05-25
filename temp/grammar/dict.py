# 使用集合对列表去重的示例代码

# 1. 原始列表（包含重复元素）
original_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
print("原始列表:", original_list)

# 2. 使用集合去重的步骤
# 步骤1: 将列表转换为集合（自动去重）
temp_set = set(original_list)
print("转换为集合:", temp_set)

# 步骤2: 将集合转换回列表
unique_list = list(temp_set)
print("去重后的列表:", unique_list)

# 3. 一行代码实现去重（常用方法）
unique_list_one_line = list(set(original_list))
print("一行代码去重:", unique_list_one_line)

# 4. 保留原始顺序的去重方法
# 注意：集合是无序的，所以上面的方法会打乱顺序
# 如果需要保留原始顺序，可以使用以下方法
def deduplicate_preserve_order(lst):
    seen = set()  # 用于记录已出现的元素
    result = []   # 用于存储去重后的结果
    for item in lst:
        if item not in seen:
            seen.add(item)  # 将元素添加到集合中
            result.append(item)  # 将元素添加到结果列表中
    return result

ordered_unique_list = deduplicate_preserve_order(original_list)
print("保留顺序的去重列表:", ordered_unique_list)
