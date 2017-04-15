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

finalkey=[]
finalkey.append(' '.join(keyword_htc))
finalkey.append(' '.join(keyword_sam))
finalkey.append(' '.join(keyword_apple))
finalkey.append(' '.join(keyword_xm))
finalkey.append(' '.join(keyword_sony))
finalkey.append(' '.join(keyword_lg))
finalkey.append(' '.join(keyword_asus))


vectorizer=CountVectorizer()
transformer=TfidfTransformer()
tfidf=transformer.fit_transform(vectorizer.fit_transform(finalkey))
y = np.array([1,2,3,4,5,6,7])#1:htc 2:samsung 3:apple 4:xiaomi 5:sony 6:lg 7:asus
clf = MultinomialNB().fit(tfidf, y)



testcontent="samsung手機好嗎?"
testword= convert_doc_to_wordlist(testcontent,False)
testkey=[]
testkey.append(' '.join(testword))

testset=transformer.fit_transform(vectorizer.transform(testkey))
print(clf.predict(testset))



































