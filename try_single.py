import os
import shutil

#尝试单个归档关系的存储
# 定义要复制到的目标路径
dest_dir = '/home/data/zhangyixuan/MG_Huiying_archive/99000001'

# 定义要复制的源路径列表
parent_dir_info = ['/home/data/zhangyixuan/MG_Huiying_bk/乳腺MG-肿块-6.1-6.30/411279/0000153075']

for parent_dir in parent_dir_info:
    txt_files = [f for f in os.listdir(parent_dir) if f.endswith('.txt')]
    for txt_file in txt_files:
        # 复制txt文件到目标位置
        source_file = os.path.join(parent_dir, txt_file)
        dest_file = os.path.join(dest_dir, txt_file)
        print(txt_file)
        shutil.copy(source_file, dest_file)
        print(f"Successfully copied {txt_file} from {parent_dir} to {dest_dir}")