# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 03:16:32 2020

@author: sihan
"""
import os 
import numpy as np
path = os.getcwd() + '\\24787_ML_project_data\\MD_data'
files = os.listdir(path)

#%%
# 只保留含有mass的字符串
files2 = []
for file in files:
    if file[0:4] == 'mass':
        files2.append(file)
        
files = files2.copy()

#%%
y = np.empty((0,100))

#%% 进入一个文件夹下
for i in range(len(files)):
   
    subfolder = files[i]
    subpath = path + '\\' + subfolder
    
    #%% 在进入下一级文件夹
    
    subfiles = os.listdir(subpath)
    subfiles2 = []
    for file in subfiles:
        if file[0:4] == 'mass':
            subfiles2.append(file)
    
    subfiles = subfiles2.copy()
    
    #%%
    # 真的进入了
    for j in range(len(subfiles)):
        subsubfolder = subfiles[j]
        subsubpath = subpath +'\\' + subsubfolder
        
        # 阅读到profile数据
        data_files = os.listdir(subsubpath)[0]
        
        #打开profiles数据
        with open(subsubpath + "\\" + data_files) as f:
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

#%%
# 变成迭代器
np.save('y_data', y)
#遍历行




















# iter_f = iter(f)
# count = 1
# record = np.array([])
# for line in iter_f:
#     if count>=5:
#         pass
#         # print(len(line))
#         # np.append(record, line, axis=0)
        
#     count = count+1
