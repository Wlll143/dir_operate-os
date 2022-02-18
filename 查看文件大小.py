"""
@ User ： 李文杰
------------------------
@ Time ： 2022/2/18 1:32
@ Name ： 查看文件大小.py
------------------------
"""

import os

# 对文件夹遍历并返回文件夹大小
def folder_file_size(folder_path):
    try:
        name = os.listdir(folder_path)
        all_size = 0
        for i in name:
            all_name = os.path.join(folder_path, i)
            if os.path.isdir(all_name) == True:
                size_folder = folder_file_size(all_name)
                all_size = all_size + size_folder
            else:
                size_file = os.path.getsize(all_name)
                all_size = all_size + size_file
        return all_size
    except:
        print("报错")
        return 0

# 用于转换文件大小单位
def K_M_G(size):
    if size >= 1024:
        k = size / 1024
        xiaoshu = size % 1024
    else:
        return f'{int(size)}B'
    if k >= 1024:
        m = k / 1024
        k = k % 1024
    else:
        return f"{int(k)}KB, {int(xiaoshu)}B"
    if m >= 1024:
        g = m / 1024
        m = m % 1024
        return f"{int(g)}GB,{int(m)}MB"
    else:
        return f"{int(m)}MB,{int(k)}KB"


if __name__ == '__main__':

    path_1 = input("请输入需要查询的文件夹（文件）位置：")
    name = os.listdir(path_1)
    with open(f"{os.path.basename(path_1)}位置的文件大小.txt", 'w') as f:
        for i in name:
            all_name = os.path.join(path_1, i)
            if os.path.isfile(all_name) == True:
                f.writelines(i + '    :          ' + K_M_G(os.path.getsize(all_name)) + '\n')
                print(i, ":", K_M_G(os.path.getsize(all_name)))
            else:
                f.writelines(i + "    :          " + K_M_G(folder_file_size(all_name)) + '\n')
                print(i, ":", K_M_G(folder_file_size(all_name)))
