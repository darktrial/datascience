import json
from pprint import pprint
import jieba
import re
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] 
    mpl.rcParams['axes.unicode_minus'] = False 

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, "%s" % float(height))


def convert_doc_to_wordlist(str_doc,cut_all):
    sent_list = str_doc.split('\n')
    sent_list = map(rm_char, sent_list)
    word_2dlist = [rm_tokens(jieba.cut(part,cut_all=cut_all)) for part in sent_list]
    word_list = sum(word_2dlist,[])
    return word_list

def rm_char(text):
    text = re.sub('\u3000','',text)
    return text

def get_stop_words(path="stop_word.txt"):
    file = open(path,'rb').read().decode('utf8').split('\r\n')
    return set(file)

def rm_tokens(words): 
    words_list = list(words)
    stop_words = get_stop_words()
    #print(stop_words)
    for i in range(words_list.__len__())[::-1]:
        if words_list[i] in stop_words: 
            words_list.pop(i)
        elif words_list[i].isdigit():
            words_list.pop(i)
    return words_list
    
def display_scores(vectorizer, tfidf_result):
    count=0
    scores = zip(vectorizer.get_feature_names(),np.asarray(tfidf_result.sum(axis=0)).ravel())
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for item in sorted_scores:
        count+=1
        if (count>10):
            break
        #print ("{0:3} Score: {1}".format(item[0], item[1]))
        print(item[0],item[1])

def display_graph(vectorizer, tfidf_result,brand_name,max_data=10):
    itemlist=[]
    scorelist=[]
    count=0
    plt.figure()
    plt.xlabel(u"關鍵字")
    plt.ylabel(u"分數")
    plt.title(u"廠牌關鍵字分析")
    scores = zip(vectorizer.get_feature_names(),np.asarray(tfidf_result.sum(axis=0)).ravel())
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for item in sorted_scores:
        count+=1
        if (count>max_data):
            break
        itemlist.append(item[0])
        scorelist.append(item[1])
        #print ("{0:3} Score: {1}".format(item[0], item[1]))
        #print(item[0],item[1])
    plt.xticks((0,1,2,3,4,5,6,7,8,9),(itemlist[0],itemlist[1],itemlist[2],itemlist[3],itemlist[4],itemlist[5],itemlist[6],itemlist[7],itemlist[8],itemlist[9]))
    rect = plt.bar(left = (0,1,2,3,4,5,6,7,8,9),height = (scorelist[0],scorelist[1],scorelist[2],scorelist[3],scorelist[4],scorelist[5],scorelist[6],scorelist[7],scorelist[8],scorelist[9]),width = 0.35,align="center")    
    plt.legend((rect,),(brand_name,))
    autolabel(rect)
    set_ch()
    plt.show()

allcontent_htc=""
allcontent_sam=""
allcontent_apple=""
allcontent_xm=""
allcontent_sony=""
allcontent_lg=""
allcontent_asus=""
with open('train_data.json',encoding = 'utf8')  as content_file:       
    for line in content_file:
        item=json.loads(line)
        #print(item['title'])
        if ('htc' in ''.join(item['brand'])):
            allcontent_htc=allcontent_htc+''.join(item['title'])+''.join(item['content'])
        elif ('sam' in ''.join(item['brand'])):
            allcontent_sam=allcontent_sam+''.join(item['title'])+''.join(item['content'])
        elif ('apple' in ''.join(item['brand'])):
            allcontent_apple=allcontent_apple+''.join(item['title'])+''.join(item['content'])
        elif ('xm' in ''.join(item['brand'])):
            allcontent_xm=allcontent_xm+''.join(item['title'])+''.join(item['content'])
        elif ('sony' in ''.join(item['brand'])):
            allcontent_sony=allcontent_sony+''.join(item['title'])+''.join(item['content'])
        elif ('lg' in ''.join(item['brand'])):
            allcontent_lg=allcontent_lg+''.join(item['title'])+''.join(item['content'])
        elif ('asus' in ''.join(item['brand'])):
            allcontent_asus=allcontent_asus+''.join(item['title'])+''.join(item['content'])
        else:
            print("")


keyword_htc = convert_doc_to_wordlist(allcontent_htc,False)
keyword_sam = convert_doc_to_wordlist(allcontent_sam,False)           
keyword_apple = convert_doc_to_wordlist(allcontent_apple,False)    
keyword_xm = convert_doc_to_wordlist(allcontent_xm,False)    
keyword_sony = convert_doc_to_wordlist(allcontent_sony,False)    
keyword_lg = convert_doc_to_wordlist(allcontent_lg,False)    
keyword_asus = convert_doc_to_wordlist(allcontent_asus,False)    


vectorizer_htc=CountVectorizer()
transformer_htc=TfidfTransformer()
tfidf_htc=transformer_htc.fit_transform(vectorizer_htc.fit_transform(keyword_htc))

vectorizer_sam=CountVectorizer()
transformer_sam=TfidfTransformer()
tfidf_sam=transformer_sam.fit_transform(vectorizer_sam.fit_transform(keyword_sam))

vectorizer_apple=CountVectorizer()
transformer_apple=TfidfTransformer()
tfidf_apple=transformer_apple.fit_transform(vectorizer_apple.fit_transform(keyword_apple))

vectorizer_xm=CountVectorizer()
transformer_xm=TfidfTransformer()
tfidf_xm=transformer_xm.fit_transform(vectorizer_xm.fit_transform(keyword_xm))

vectorizer_sony=CountVectorizer()
transformer_sony=TfidfTransformer()
tfidf_sony=transformer_sony.fit_transform(vectorizer_sony.fit_transform(keyword_sony))

vectorizer_lg=CountVectorizer()
transformer_lg=TfidfTransformer()
tfidf_lg=transformer_lg.fit_transform(vectorizer_lg.fit_transform(keyword_lg))

vectorizer_asus=CountVectorizer()
transformer_asus=TfidfTransformer()
tfidf_asus=transformer_asus.fit_transform(vectorizer_asus.fit_transform(keyword_asus))


print("***HTC list***")
display_graph(vectorizer_htc,tfidf_htc,"htc")
print("***Samsung list***")
display_graph(vectorizer_sam,tfidf_sam,"samsung")
print("***Apple list***")
display_graph(vectorizer_apple,tfidf_apple,"apple")
print("***XiaoMi list***")
display_graph(vectorizer_xm,tfidf_xm,"xiaomi")
print("***Sony list***")
display_graph(vectorizer_sony,tfidf_sony,"sony")
print("***LG list***")
display_graph(vectorizer_lg,tfidf_lg,"lg")
print("***ASUS list***")
display_graph(vectorizer_asus,tfidf_asus,"asus")



"""
word=vectorizer.get_feature_names()
weight=tfidf.toarray()

for i in range(len(weight)):
    print("the ",i,"sample")
    for j in range(len(word)):  
        print (word[j],weight[i][j])
"""