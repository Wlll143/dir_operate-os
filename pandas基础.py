"""
@ User ： Wlll
------------------------
@ Time ： 2022/2/19 14:58
@ Name ： pandas基础.py
------------------------
"""

import pandas as pd
import numpy as np


# 创建DataFrame，索引，修改索引
def Found():
    # 创建二维数组
    data = pd.DataFrame(np.arange(1, 10).reshape(3, 3), index=[1, 2, 3], columns=["A", "B", "C"])
    print(data)
    print('\n')

    # 索引的命名，修改
    data.index.name = "数字"
    print(data, '\n')
    data = data.rename(index={1: "yi", 2: "er", 3: "san"}, columns={"A": "1lie", "B": "2lie", "C": "3lie"})
    print(data, '\n')

    # pd.DataFrame.from_dict({},orient="index")可以从字典传递，参数orient用于指定以字典的键名作为列索引还是行索引，
    # 默认值为'columns'，即以字典的键名作为列索引，如果设置成'index'，则表示以字典的键名作为行索引

    # 如果想将行索引转换为常规列，可以用reset_index()函数重置索引
    data = data.reset_index()
    print(data, '\n')


# 读取和写入文件
"""
读取文件：
pd.read_excel()
·sheetname用于指定工作表，可以是工作表名称，也可以是数字（默认为0，即第1个工作表）。
·encoding用于指定文件的编码方式，一般设置为UTF-8或GBK编码，以避免中文乱码。
·index_col用于设置索引列。
pd.read_csv()
·delimiter用于指定CSV文件的数据分隔符，默认为逗号。
·encoding用于指定文件的编码方式，一般设置为UTF-8或GBK编码，以避免中文乱码。
·index_col用于设置索引列。

写入文件:
data.to_excel("path")
·sheetname用于指定工作表名称。
·index用于指定是否写入行索引信息，默认为True，即将行索引信息存储在输出文件的第1列；若设置为False，则忽略行索引信息。
·columns用于指定要写入的列。
·encoding用于指定编码方式。
"""


# 数据查找,筛选
def seek():
    data = pd.DataFrame(np.arange(1, 10).reshape(3, 3), index=[1, 2, 3], columns=["A", "B", "C"])
    a = data["C"]  # 返回一维的
    a1 = data[['C']]  # 返回二维的,返回多列需要用这个
    print(a, a1)

    # 选取多少行到多少行
    # iloc(行序号选取)(用数字作为索引)
    b = data.iloc[0:2]  # 左闭右开
    print(b)
    # loc(行名称选取)(用字符串作为索引)
    b1 = data.loc[[1, 2]]
    print(b1)

    # 数据筛选
    # 如果有多个筛选条件，可以用“&”（表示“且”）或“|”（表示“或”）连接起来。
    b = data[(data['c1'] > 1) & (data['c2'] == 5)]


# 数据排序
def sort():
    data = pd.DataFrame(np.arange(1, 10).reshape(3, 3), index=[1, 2, 3], columns=["A", "B", "C"])
    # 参数by用于指定按哪一列来排序；
    # 参数ascending（“上升”的意思）默认值为True，表示升序排序，若设置为False则表示降序排序。
    a = data.sort_values(by='A', ascending=False)
    print(a)
    # 使用sort_index()函数可以按行索引进行排序
    a1 = data.sort_index(ascending=False)
    print(a1)


# 数据运算，删除
def calculation():
    # 数据计算，可以生成不存在的一列
    data = pd.DataFrame(np.arange(1, 10).reshape(3, 3), index=[1, 2, 3], columns=["A", "B", "C"])
    data["D"] = data["C"] - data["A"]
    print(data)

    # 数据删除
    # data.drop()
    # ·index用于指定要删除的行。
    # ·columns用于指定要删除的列。
    # ·inplace默认值为False，表示该删除操作不改变原DataFrame，而是返回一个执行删除操作后的新DataFrame，如果设置为True，则会直接在原DataFrame中进行删除操作。
    # 给出行索引时要输入行索引名称而不是数字序号，除非行索引名称本来就是数字。
    a = data.drop(columns="A")  # columns=["A","B"]
    print(a)


# 数据表的拼接
def data_join():
    data1 = pd.DataFrame(np.arange(1, 10).reshape(3, 3), index=[1, 2, 3], columns=["A", "B", "C"])
    data2 = pd.DataFrame(np.arange(1, 10).reshape(3, 3), index=[1, 2, 3], columns=["A", "B", "D"])
    print(data1)
    print(data2)

    # merge()函数可以根据一个或多个同名的列将不同数据表中的行连接起来(不存在相同的值则为空)
    # 如果同名的列不止一个，可以通过设置参数on指定按照哪一列进行合并
    # 默认的合并方式其实是取交集（inner连接），即选取两个表共有的内容。
    a = pd.merge(data1, data2, on="A")
    # 如果想取并集（outer连接），即选取两个表所有的内容，可以设置参数how
    a1 = pd.merge(data1, data2, on="A", how="outer")
    # 如果想保留左表的全部内容，而对右表不太在意，可以将参数how设置为"left"
    a2 = pd.merge(data1, data2, how="left")
    # 如果想按照行索引进行合并，可以设置参数left_index和right_index
    a3 = pd.merge(data1, data2, left_index=True, right_index=True)
    print(a, '\n', a1, '\n', a2, '\n', a3)

    # concat()函数使用全连接（UNION ALL）方式完成拼接，
    # 它不需要对齐，而是直接进行合并，即不需要两个表有相同地列或索引，只是把数据整合到一起
    # 参数axis指定连接的轴向。该参数默认值为0，指按行方向连接（纵向拼接）
    b = pd.concat([data1, data2], axis=0)
    # 参数ignore_index为True来忽略原有索引，生成新的数字序列作为索引
    b1 = pd.concat([data1, data2], axis=0, ignore_index=True)

    print(b, '\n', b1)

    # append()函数可以看成concat()函数的简化版，效果和pd.concat([df1,df2])类似，实现的也是纵向拼接
    # 可以新增元素
    # 这里一定要设置参数ignore_index为True来忽略原索引，否则会报错
    c = data1.append({"A": 10, "C": 100}, ignore_index=True)
    print(c)


if __name__ == '__main__':
    pass
