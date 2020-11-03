# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:51:25 2020

@author: sihan
"""
import os 
import numpy as np
path = os.getcwd() + '\\24787_ML_project_data\\tempdata'
files = os.listdir(path)

y = np.empty((0,100))
x = np.empty((0,2))

# 遍历每个文件

for i in range(len(files)):
    file = files[i]
    with open(path + "\\" + file) as f:
        # read_data = f.read()
        one_file_data = []
        count = 1 
        for lines in f:
            if count >= 5:
                one_row = lines.split()
                one_file_data.append(float(one_row[3]))
            count = count + 1
    
    one_file_data = np.array(one_file_data).reshape((-1,100))
                
    y = np.append(y, one_file_data, axis=0)
    
    # 获取x
    one_x = np.array([[float(file[5:7]), float(file[10:13])]])
    one_x = one_x.reshape((-1,2))
    x = np.append(x, one_x, axis=0)
    
data = np.append(x,y,axis=1)
np.save('y_data2.npy', y)
np.save('x_data2.npy', x)
np.save('data.npy2', data)
