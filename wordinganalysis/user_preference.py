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
import operator

htc_dict = {}
samsung_dict={}
apple_dict={}
xm_dict={}
sony_dict={}
lg_dict={}
asus_dict={}



with open('train_data.json',encoding = 'utf8')  as content_file:       
    for line in content_file:
        item=json.loads(line)
        if ('htc' in ''.join(item['brand'])):
            for i in range(len(item['positive_user'])):
                if (item['positive_user'][i].replace(" ", "") in htc_dict):
                    htc_dict[item['positive_user'][i].replace(" ", "")]+=1
                else:
                   htc_dict.update({item['positive_user'][i].replace(" ", ""):1}) 
        elif ('sam' in ''.join(item['brand'])):
            for i in range(len(item['positive_user'])):
                if (item['positive_user'][i].replace(" ", "") in samsung_dict):
                    samsung_dict[item['positive_user'][i].replace(" ", "")]+=1
                else:
                   samsung_dict.update({item['positive_user'][i].replace(" ", ""):1})  
        elif ('apple' in ''.join(item['brand'])):
            for i in range(len(item['positive_user'])):
                if (item['positive_user'][i].replace(" ", "") in apple_dict):
                    apple_dict[item['positive_user'][i].replace(" ", "")]+=1
                else:
                   apple_dict.update({item['positive_user'][i].replace(" ", ""):1}) 
        elif ('xm' in ''.join(item['brand'])):
            for i in range(len(item['positive_user'])):
                if (item['positive_user'][i].replace(" ", "") in xm_dict):
                    xm_dict[item['positive_user'][i].replace(" ", "")]+=1
                else:
                   xm_dict.update({item['positive_user'][i].replace(" ", ""):1}) 
        elif ('sony' in ''.join(item['brand'])):
            for i in range(len(item['positive_user'])):
                if (item['positive_user'][i].replace(" ", "") in sony_dict):
                    sony_dict[item['positive_user'][i].replace(" ", "")]+=1
                else:
                   sony_dict.update({item['positive_user'][i].replace(" ", ""):1}) 
        elif ('lg' in ''.join(item['brand'])):
            for i in range(len(item['positive_user'])):
                if (item['positive_user'][i].replace(" ", "") in lg_dict):
                    lg_dict[item['positive_user'][i].replace(" ", "")]+=1
                else:
                   lg_dict.update({item['positive_user'][i].replace(" ", ""):1})
        elif ('asus' in ''.join(item['brand'])):
            for i in range(len(item['positive_user'])):
                if (item['positive_user'][i].replace(" ", "") in asus_dict):
                    asus_dict[item['positive_user'][i].replace(" ", "")]+=1
                else:
                   asus_dict.update({item['positive_user'][i].replace(" ", ""):1}) 
        else:
            print("")

x=htc_dict
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
sorted_x.reverse()
for i in range(0,9):
    print(sorted_x[i])


def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] 
    mpl.rcParams['axes.unicode_minus'] = False 

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, "%s" % float(height))

set_ch()

plt.figure()

plt.xlabel(u"愛好者")
plt.ylabel(u"愛好程度")

plt.title(u"HTC愛好者程度分析")    
plt.xticks((0,1,2,3,4,5,6,7,8),(sorted_x[0][0],sorted_x[1][0],sorted_x[2][0],sorted_x[3][0],sorted_x[4][0],sorted_x[5][0],sorted_x[6][0],sorted_x[7][0],sorted_x[8][0]))

rect = plt.bar(left = (0,1,2,3,4,5,6,7,8,),height = (sorted_x[0][1],sorted_x[1][1],sorted_x[2][1],sorted_x[3][1],sorted_x[4][1],sorted_x[5][1],sorted_x[6][1],sorted_x[7][1],sorted_x[8][1]),width = 0.35,align="center")

plt.legend((rect,),(u"HTC愛好者分析",))
autolabel(rect)

plt.show()

person="james732"
print("htc favorite:",htc_dict[person], \
      "samsung favorite:",samsung_dict[person], \
      "apple favorite:",apple_dict[person], \
      "xm favorite:",xm_dict[person], \
      "sony favorite:",sony_dict[person], \
      "lg favorite:",lg_dict[person], \
      "asus favorite:",asus_dict[person])

plt.figure()

plt.xlabel(u"手機品牌")
plt.ylabel(u"愛好程度")

plt.title("愛好者程度分析") 

plt.xticks((0,1,2,3,4,5,6),("htc","samsung","apple","xiaomi","sony","lg","asus"))
rect = plt.bar(left = (0,1,2,3,4,5,6,),height = (htc_dict[person],samsung_dict[person],apple_dict[person],xm_dict[person],sony_dict[person],lg_dict[person],asus_dict[person]),width = 0.35,align="center")

plt.legend((rect,),(person,))
autolabel(rect)

plt.show()
            
            
        