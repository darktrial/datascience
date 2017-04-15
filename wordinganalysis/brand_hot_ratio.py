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

htc_positive_count=0
samsung_positive_count=0
apple_positive_count=0
xm_positive_count=0
sony_positive_count=0
lg_positive_count=0
asus_positive_count=0

with open('train_data.json',encoding = 'utf8')  as content_file:       
    for line in content_file:
        item=json.loads(line)
        if ('htc' in ''.join(item['brand'])):
            htc_positive_count+=int(''.join(item['positive_count']))
        elif ('sam' in ''.join(item['brand'])):
            samsung_positive_count+=int(''.join(item['positive_count']))
        elif ('apple' in ''.join(item['brand'])):
            apple_positive_count+=int(''.join(item['positive_count']))
        elif ('xm' in ''.join(item['brand'])):
            xm_positive_count+=int(''.join(item['positive_count']))
        elif ('sony' in ''.join(item['brand'])):
            sony_positive_count+=int(''.join(item['positive_count']))
        elif ('lg' in ''.join(item['brand'])):
            lg_positive_count+=int(''.join(item['positive_count']))
        elif ('asus' in ''.join(item['brand'])):
            asus_positive_count+=int(''.join(item['positive_count']))
        else:
            print("")


#print(htc_positive_count, samsung_positive_count,xm_positive_count, sony_positive_count,lg_positive_count,asus_positive_count)

def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] 
    mpl.rcParams['axes.unicode_minus'] = False 

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, "%s" % float(height))

set_ch()

plt.xlabel(u"熱門程度")
plt.ylabel(u"品牌")

plt.title(u"品牌熱門程度分析")

plt.xticks((0,1,2,3,4,5,6),("htc","samsung","apple","xiaomi","sony","lg","asus"))
rect = plt.bar(left = (0,1,2,3,4,5,6,),height = (htc_positive_count,samsung_positive_count,apple_positive_count,xm_positive_count,sony_positive_count,lg_positive_count,asus_positive_count),width = 0.35,align="center")

plt.legend((rect,),(u"品牌手機討論度分析",))
autolabel(rect)

plt.show()
        