import os
import glob

#用于删除被重复复制的txt文件
# 读取父目录信息文件
file_path = '/home/data/zhangyixuan/Exp/final_corr.txt'  # 请替换为您的txt文档路径
# 假设 parent_dir_info 是包含多个源目录路径的列表
parent_dir_info = []
dest_paths = []
with open(file_path, 'r') as file:
    for line in file:
        columns = line.strip().split(' - ')
        if len(columns) >= 2:
            # path = columns[0].split(',')[0]
            path1 = columns[1].split(',',)[0]
            # print(path)
            # print(path1)
            # parent_dir_info.append(path)
            dest_paths.append(path1)
print(dest_paths)

# 在每个路径中查找并删除 .txt 文件
deleted_files = []

for dir_path in dest_paths:
    # 使用 glob 递归查找 .txt 文件
    txt_files = glob.glob(os.path.join(dir_path, '**/*.txt'), recursive=True)

    for txt_file in txt_files:
        if os.path.isfile(txt_file):  # 确保删除的是文件而不是目录
            os.remove(txt_file)
            deleted_files.append(txt_file)

# 输出删除的文件列表用于验证
print('Deleted files:')
for deleted_file in deleted_files:
    print(deleted_file)