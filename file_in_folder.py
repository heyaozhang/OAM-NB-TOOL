#!/usr/bin/env python
# -*- coding: utf-8 -*-

allfile = []
def get_all_file(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path,file)
        # 判断是否是文件夹
        if os.path.isdir(filepath):
            get_all_file(filepath)
        # 是文件就将路径添加到列表
        allfile.append(filepath)
    return allfile
