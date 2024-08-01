import os
import csv
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(4096)  # 读取文件内容前4K字节用于检测编码
        result = chardet.detect(raw_data)
        return result['encoding']

def extract_diagnosis_text(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
        if ';;diagnosis:' in content:
            diagnosis_text = content.split(';;diagnosis:')[-1].strip()
            return diagnosis_text
    return None

def extract_target_directory(file_path):
    parts = file_path.split(os.sep)
    if len(parts) > 2:
        return parts[-3]  # 提取包含目标的部分
    return None

def main():
    root_directory = '/home/data/zhangyixuan/MG_Huiying_archive1'
    output_csv = 'diagnosis_output.csv'
    all_diagnosis_texts = {}

    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Target Directory', 'File Path', 'Diagnosis']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for foldername, subfolders, filenames in os.walk(root_directory):
            for filename in filenames:
                if filename.endswith('.txt'):
                    file_path = os.path.join(foldername, filename)
                    diagnosis_text = extract_diagnosis_text(file_path)
                    target_directory = extract_target_directory(file_path)
                    if diagnosis_text and target_directory:
                        all_diagnosis_texts[file_path] = diagnosis_text
                        writer.writerow({'Target Directory': target_directory,
                                         'File Path': file_path,
                                         'Diagnosis': diagnosis_text})

    # 输出结果
    for filepath, diagnosis in all_diagnosis_texts.items():
        target_directory = extract_target_directory(filepath)
        print(f'{target_directory} - {filepath}: {diagnosis}')

if __name__ == '__main__':
    main()