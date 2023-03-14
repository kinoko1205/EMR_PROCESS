import os
import operator
import re
import csv

def getdata(data_path):
    contents = []   # 存放txt文件每行的内容
    data = []
    star = []
    data_final = []
    path1 ='./example/'
    path2 = data_path
    path3 = path1 + path2
    files_1 = os.listdir(path3)
    for file1 in files_1:
        pos = path3 + '/' + file1  # filename
        with open(pos, 'r', encoding='utf-8') as f:     # encoding='utf-8'不行
            contents = f.read()
            data.append(contents)
            f.close()
    for i in range(len(data)):
        star = data[i] + '\n'
        data_final.append(star)
    filedir = './preprocessed/'
    filename = filedir + data_path + '.txt'
    with open(filename , 'w', encoding='utf-8') as f_object:
        f_object.write(' '.join(data_final))
        f_object.close()
