
import os
import shutil
import glob

#复制txt文件到归档好的指定位置
# 读取父目录信息文件
file_path = '/home/data/zhangyixuan/Exp/final_corr.txt'  # 请替换为您的txt文档路径

parent_dir_info = []
dest_paths = []
with open(file_path, 'r') as file:
    for line in file:
        columns = line.strip().split(' - ')
        if len(columns) >= 2:
            path = columns[0].split(',')[0]
            path1 = columns[1].split(',',)[0]
            # print(path)
            # print(path1)
            parent_dir_info.append(path)
            dest_paths.append(path1)
print(parent_dir_info)

# 确保源目录和目标目录列表长度一致
assert len(parent_dir_info) == len(dest_paths), "源目录列表和目标目录列表长度不一致"

# 遍历每个源目录和对应的目标目录
for src_dir, dest_dir in zip(parent_dir_info, dest_paths):
    txt_files = glob.glob(os.path.join(src_dir, '**/*.txt'), recursive=True)
    os.makedirs(dest_dir, exist_ok=True)  # 创建目标目录如果不存在
    for txt_file in txt_files:
        shutil.copy(txt_file, dest_dir)

print('文件一对一复制完成')
