import os

import pydicom
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def dcm_to_png(dcm_file, png_file):
    # 读取DICOM文件
    ds = pydicom.dcmread(dcm_file)

    # 获取图像数据
    img_array = ds.pixel_array

    # 将图像数据转换为8位（0-255）
    img_array = img_array - np.min(img_array)
    img_array = img_array / np.max(img_array)
    img_array = (img_array * 255).astype(np.uint8)

    # 创建Pillow图像
    img = Image.fromarray(img_array)

    # 保存为PNG文件
    img.save(png_file)
    # print(f"Converted {dcm_file} to {png_file}")


# 示例用法
if __name__ == '__main__':
    general_path = r"D:\DataSet\Huiying_99_1"
    l1_list = os.listdir(general_path)
    for l1_path in l1_list:
        l2_path = os.path.join(os.path.join(general_path, l1_path), "st01")
        dcm_file = os.listdir(l2_path)
        out_path = os.path.join("D:\label_png1", l1_path)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        for file in dcm_file:
            if file.lower().endswith('.dcm'):
                name = file[0:-4]
                print(name)
                dcm_path = os.path.join(l2_path, file)
                output_file = os.path.join(out_path,name+".png")
                dcm_to_png(dcm_path, output_file)
    #             print(f"DICOM文件 {dcm_file} 已成功转换为 {output_png}")
    #
    # dcm_file = r'D:\PycharmProjects\patch_yolo8\label_data\99000041\st01\p9900004101cl.dcm'  # 替换为你的DICOM文件路径
    # output_png = 'output_image.png'  # 输出PNG文件路径
    # dcm_to_png(dcm_file, output_png)
    # print(f"DICOM文件 {dcm_file} 已成功转换为 {output_png}")
