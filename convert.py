import os
# 遍历目录下所有的txt，得到相对地址列表
# 指定路径
path = '/home/data/zhangyixuan/MG_Huiying_bk1'

# 创建一个用于保存txt文件路径及其所在目录的上一级目录的上一级目录名称的txt文件
output_file = open('patient_id.txt', 'w')

# 遍历所有文件和文件夹
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            parent_directory = os.path.basename(os.path.dirname(file_path))  # 获取txt文件所在目录的上一级目录名称
            parent_parent_directory = os.path.basename(os.path.dirname(root)) # 获取txt文件所在目录的上一级目录的上一级目录名称
            output_file.write(f'{file_path},{parent_parent_directory}\n')  # 写入路径和上一级目录的上一级目录名称到txt文件

# 关闭txt文件
output_file.close()