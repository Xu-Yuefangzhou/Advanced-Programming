__author__ = 'Jane_Xu'
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:14:14 2018

@author: Jane Xu

Reference：
1.https://www.cnblogs.com/coskaka/articles/5965091.html
2.https://www.cnblogs.com/zhbzz2007/p/6001827.html
3.https://www.jianshu.com/p/4bd8a1c93cbe

"""

import functools #用于高阶函数：指那些作用于函数或者返回其它函数的函数，通常只要是可以被当做函数调用的对象就是这个模块的目标。
#定义文件读取函数，并且输出元素为词频的字典
from nltk.corpus import stopwords

def readFile(file_name):
    y = []
    with open(file_name, 'r', encoding="utf-8") as f:
        x = f.readlines()
    for line in x:
        y.extend(line.split())
    word_list2=[]
    
    # 单词格式化：去掉分词之后部分英文前后附带的标点符号
    for word in y:
        #每个单词最后一个字母
        word1 = word
        #标点
        while True:
            lastchar = word1[-1:]
            if lastchar in [",", ".", "!", "?", ";", '"']:
                word2 = word1.rstrip(lastchar)
                word1 = word2
            else:
                word2 = word1
                break
        while True:
            firstchar = word2[0]
            if firstchar in [",", ".", "!", "?", ";", '"']:
                word3 = word2.lstrip(firstchar)
                word2 = word3
            else:
                word3 = word2
                break
        #if word3 not in stopwords.words('english'):
        word_list2.append(word3)
        #for word in word_list2:
  
    #统计词频
    tf = {}    
    for word in word_list2:
        word = word.lower()
        word = ''.join(word.split())
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1
    return tf
    
def get_counts(words):
    tf = {}
    for word in words:
        word = word.lower()
        word = ''.join(word.split())
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1

#合并
def merge2(dic1, dic2):
    from collections import Counter
    counts = Counter(dic1) + Counter(dic2)
    return counts

def top_counts(word_list,n=10):
     value_key_pairs = sorted([(count, tz) for tz, count in word_list.items()],reverse = True)
     return value_key_pairs[:n]
     
     
def last_counts(word_list,n=10):
     value_key_pairs = sorted([(count, tz) for tz, count in word_list.items()])
     return value_key_pairs[:n]     

if __name__ == '__main__':
     file_list = [r'1.txt',
                     r'2.txt',
                     r'3.txt',
                     r'4.txt',
                     r'5.txt',]
 
     cc=map(readFile,file_list)
     word_list = functools.reduce(merge2,cc)
     top_counts=top_counts(word_list)
     last_counts=last_counts(word_list)
     # print(top_counts)
     print ('Top 10:')
     for word in top_counts[0:10]:
         print("{0:10}{1}".format(word[1], word[0]))
        
     print ('\nLast 10:')
     for word in last_counts[0:10]:
         print("{0:10}{1}".format(word[1], word[0]))