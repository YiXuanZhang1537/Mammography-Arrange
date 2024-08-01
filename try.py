# import os
# # 读取列表1数据
# base_path = '/home/data/zhangyixuan/MG_Huiying_bk'
# with open('/home/data/zhangyixuan/Exp/patient_id.txt', 'r') as file:
#     list1 = [line.strip() for line in file]
#
# # 读取列表2数据
# with open('/home/data/zhangyixuan/MG_Huiying_archive/HUIYI.lst', 'r') as file:
#     list2 = [line.strip() for line in file]
#
# # 保存找到的结果的文件
# found_file = open('found_new_id.txt', 'w')
# not_found_file = open('no_corr_id.txt', 'w')
#
# # 保存找到的匹配信息的文件
# final_corr_file = open('final_corr.txt', 'w')
# # 遍历列表1中的元素
# for item1 in list1:
#     found = False
#     # 在列表2中查找匹配项
#     for item2 in list2:
#         if item1 in item2:
#             data1, data2 = item1, item2.split()[0]
#             print(f"Found: {data1} in list 2 corresponding to {data2}")
#             found_file.write(f"Found: {data1} in list 2 corresponding to {data2}\n")
#             found = True
#             folders = [folder for folder in os.listdir('/home/data/zhangyixuan/MG_Huiying_archive') if data2 in folder]
#             for folder in folders:
#                 folder_path = os.path.join('/home/data/zhangyixuan/MG_Huiying_archive/', folder)
#                 print(f"Partial match found: {folder_path} for data2: {data2} for {item1}")
#                 final_info = f"{folder_path} - {data2} - {item1}\n"
#                 final_corr_file.write(final_info)
#             break
#
#     if not found:
#         not_found_file.write(f"Not found: {item1}\n")
# found_file.close()
# not_found_file.close()

import os
#将对应关系和对应的文件位置存储起来
# 读取列表1数据
base_path = '/home/data/zhangyixuan/MG_Huiying_bk1'
with open('/home/data/zhangyixuan/Exp/patient_id.txt', 'r') as file:
    list1 = [line.strip() for line in file]

# 读取列表2数据
with open('/home/data/zhangyixuan/MG_Huiying_archive1/HUIYI.lst', 'r') as file:
    list2 = [line.strip() for line in file]

# 保存找到的结果的文件p
found_file = open('found_new_id.txt', 'w')
not_found_file = open('no_corr_id.txt', 'w')

# 保存找到的匹配信息的文件
final_corr_file = open('final_corr.txt', 'w')

def find_item_path(item):
    for root, dirs, files in os.walk(base_path):
        if item in root:
            return root
    return None

# 遍历列表1中的元素
for item1 in list1:
    found = False
    item1 = item1.split(",")[1]
    # 在列表2中查找匹配项
    for item2 in list2:
        if item1 in item2:
            data1, data2 = item1, item2.split()[0]
            print(f"Found: {data1} in list 2 corresponding to {data2}")
            found_file.write(f"Found: {data1} in list 2 corresponding to {data2}\n")
            found = True

            # 查找包含item1的路径
            item1_path = find_item_path(item1)
            if item1_path is not None:
                folders = [folder for folder in os.listdir('/home/data/zhangyixuan/MG_Huiying_archive1') if data2 in folder]
                for folder in folders:
                    folder_path = os.path.join('/home/data/zhangyixuan/MG_Huiying_archive1/', folder)
                    print(f"Partial match found: {item1_path} for {item1} and {folder_path} for {data2} for {item1}")
                    final_info = f"{item1_path} - {folder_path} - {data2} - {item1}\n"
                    final_corr_file.write(final_info)
            break

    if not found:
        not_found_file.write(f"Not found: {item1}\n")

found_file.close()
not_found_file.close()
final_corr_file.close()