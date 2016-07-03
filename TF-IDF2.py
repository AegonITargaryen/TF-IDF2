# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 15:10:20 2016

@author: Administrator
"""

import jieba
import codecs
import os 
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
"""
计算 TF-IDF

"""
inputfile="C:\\Users\\Administrator\\Desktop\\Sample\\"

stop = [line.strip().decode("utf-8") for line in open(inputfile+"StopWords.txt","r").readlines()]
#将utf-8编码格式读入，并解码为unicode python2 只能很好地处理Unicode编码

if __name__ == "__main__":
    corus=[]
    
    for i in range(10,20):
        string=u""
        with codecs.open(inputfile+"C000007\\"+str(i)+".txt","r","utf-8") as f:
            text=f.read()
        for k in jieba.cut(text):
            if k not in stop:
                string=string+k+" "
        corus.append(string)
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    
    for i in range(len(weight)):
        test=[]
        print u"-------这里输出第",i,u"类文本的词语tf-idf权重------"
        for j in range(len(word)):
            test.append([word[j],weight[i][j]])
            
        da=pd.DataFrame(test,columns=['words','counts'])
        da2=da.sort_values('counts',ascending=False)
        da2.to_csv("C:\\Users\\Administrator\\Desktop\\Sample\\"+str(i)+".csv",index=False,header=False,encoding="gbk")
        #da2.to_csv("C:\\Users\\Administrator\\Desktop\\Sample\\"+str(i)+".txt",index=False,header=False,encoding="utf-8")