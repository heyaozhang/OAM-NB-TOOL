#!/usr/bin/env python
# -*- coding: utf-8 -*-

def text_search(start,end,file_list):
    """
        在指定file_list中存在唯一起始/结束标识字符串
        用于分割指定列表
        输入
            start ==> 起始位置
            end ==> 结束位置
            file_list ==> 列表文件
        输出
            列表（从start开始所在行一直到end所在位置的前一行）

        条件
            start在file_list中唯一并存在
            end为从start开始至结尾匹配到的第一个标识字符串
            如果end没匹配到，则一直到file_list末尾
    """    
    for each in file_list:
        if start in each:
            a = file_list.index(each)
            break
        else:
            print('起始标识start不存在')
    for each in file_list[a+1:]:
        if end in each:
            b = file_list[a+1:].index(each) + 1
            break
        else:   
            b = len(file_list[a+1:])
    return file_list[a:][:b]



if __name__ == '__main__':
    f = list(open(r'test\text_search_ceshi.txt','r'))
    for each in text_search('[heyao@localhost ~]$ ifconfig','[heyao@localhost ~]',f):
        print(each)
