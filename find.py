import os
#查找原目录对应的归档目录（根据HUIYI.lst执行）

# 指定路径
path = '/home/data/zhangyixuan/MG_Huiying_archive1'

# 从mapping.lst文件中读取映射关系
mapping = {}
with open('/home/data/zhangyixuan/MG_Huiying_archive1/HUIYI.lst', 'r') as file:
    for line in file:
        key, value = line.strip().split()
        mapping[key] = value

original_search_field=[]
# 从txt文档中读取search_field
with open('/home/data/zhangyixuan/Exp/patient_id.txt', 'r') as file:
    for line in file:
        # Find the first comma in the line
        comma_index = line.find(',')
        if comma_index != -1:
            # Extract the part of the line after the first comma
            result = line[comma_index + 1:].strip()
            original_search_field.append(result)
# 遍历search_field序列，查找对应的映射字段
found_fields = []
not_found_fields = []  # 用于保存未找到匹配的值的field

for field in original_search_field:
    found_matching = False  # 标记是否找到匹配项
    for key, value in mapping.items():

        if field == value:
            # if value == "1":
            #     # 找到found_field为"1"时跳过
            #     found_matching = True
            #     continue
            found_fields.append(value)
            found_matching = True
            break  # 找到匹配项后退出内循环

    if not found_matching:
        not_found_fields.append(field)
# 为found_fields中不在original_search_field中的元素添加默认索引值
index_dict = {field: index for index, field in enumerate(original_search_field)}
for index, field in enumerate(found_fields):
    if field not in original_search_field:
        index_dict[field] = float("inf")


# 根据original_search_field中的顺序重新排列found_fields
sorted_found_fields = sorted(found_fields, key=lambda x: original_search_field.index(x) if x in original_search_field else float('inf'))



# 保存找到的文件夹路径的文件
output_file = open('found_directories.txt', 'w')

# 保存匹配的值的field和对应的key
output_file.write("匹配的值的field和对应的key:\n")
for field in found_fields:
    output_file.write(f"{field}\n")

output_file.write("\n")
#
# # 保存未找到匹配值的field
# # print(f"未找到匹配值的field:{found_fields}\n")
# # output_file.write(", ".join(not_found_fields) + "\n\n")
#
# # 保存找到的文件夹路径
# found_directories = []
# for found_field in found_fields:
#     found_match = False
#     for root, dirs, files in os.walk(path):
#         for directory in dirs:
#             parent_dir = os.path.dirname(os.path.join(root, directory))
#             print(f"Checking parent directory: {parent_dir}")  # 添加调试打印语句
#             if found_field in parent_dir:
#                 dir_path = os.path.join(root, directory)
#                 found_directories.append(f"{found_field}, {dir_path}")
#                 found_match = True
#     if not found_match:
#         print(f"No directory found for field: {found_field}")  # 添加调试打印语句
#
# output_file.close()
