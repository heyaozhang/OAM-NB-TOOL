#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Text:
    def text_search(self,start,end,file_list):
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
        self.start = start
        self.end = end
        self.file_list = file_list

        for each in self.file_list:
            if self.start in each:
                a = self.file_list.index(each)
                break

        a_exists = 'a' in locals()
        if not a_exists:
            raise UnboundLocalError('起始标识start不存在，请核查起始文本是否正确！')
        for each in self.file_list[a+1:]:
            if self.end in each:
                b = self.file_list[a+1:].index(each) + 1
                break
            else:
                b = len(self.file_list[a+1:])
        return self.file_list[a:][:b]

    def text_split(self,split_str,file_list):
        """
            在指定列表file_list中分割文本
            输入
                split_str ==> 分割标识字段
                file_list ==> 列表文件
            输出
                列表（将从起始split_str开始到文本末尾按分割字段进行分割，返回分割列表）

            条件
                split_str存在
                split_str不在最后一行
        """
        self.split_str = split_str
        self.file_list = file_list
        i = 0
        a = []
        b = []
        for each in self.file_list:
            if self.split_str in each:
                a.append(i)
            i += 1
        if a[-1] != len(self.file_list)-1:
            a.append(len(self.file_list)-1)

        j = 0
        while j < len(a)-1:
            b.append(self.file_list[a[j]:a[j+1]])
            j += 1

        return b






if __name__ == '__main__':
    f = list(open(r'test\text_search_ceshi.txt','r'))
    t = Text()
    for each in t.text_search('[heyao@localhost ~]$ ifconfig','[heyao@localhost ~]',f):
        print(each)
    for each in t.text_split('[heyao@localhost ~]$',f):
        print(each)