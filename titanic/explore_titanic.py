# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier



train_df = pd.read_csv('train.csv')
print(" Number of dead or alive:")
print(train_df['Survived'].value_counts())

#print(train_df['Survived'])
print("")
print("classify live/dead by sexual")
total_people=0
man_live=0
man_dead=0
women_live=0
women_dead=0
for index, row in train_df.iterrows():
    total_people+=1
    if (row['Survived']==1 and row['Sex']=='male'):
        man_live+=1
    if (row['Survived']==0 and row['Sex']=='male'):
        man_dead+=1    
    if (row['Survived']==1 and row['Sex']=='female'):
        women_live+=1
    if (row['Survived']==0 and row['Sex']=='female'):
        women_dead+=1

print("total people:",total_people," Dead prob:",(man_dead+women_dead)/total_people)
print("man alive:",man_live,"man_dead",man_dead,"women_live:",women_live,"women dead:",women_dead)
print("man dead prob:",man_dead/total_people,"women dead prob:",women_dead/total_people)

zero_ten=[0,0,0]
ten_twenty=[0,0,0]
twenty_thirty=[0,0,0]
thirty_forty=[0,0,0]
forty_fifty=[0,0,0]
fifty_sixty=[0,0,0]
sixty_seventy=[0,0,0]


for index, row in train_df.iterrows():
    if ((row['Age']>0 and row['Age']<10)):
        zero_ten[2]+=1
        if (row['Survived']==0):
            zero_ten[0]+=1
        else:
            zero_ten[1]+=1

    if ((row['Age']>10 and row['Age']<20)):
        ten_twenty[2]+=1
        if (row['Survived']==0):
            ten_twenty[0]+=1
        else:
            ten_twenty[1]+=1

    if ((row['Age']>20 and row['Age']<30)):
        twenty_thirty[2]+=1
        if (row['Survived']==0):
            twenty_thirty[0]+=1
        else:
            twenty_thirty[1]+=1

    if ((row['Age']>30 and row['Age']<40)):
        thirty_forty[2]+=1
        if (row['Survived']==0):
            thirty_forty[0]+=1
        else:
            thirty_forty[1]+=1

    if ((row['Age']>40 and row['Age']<50)):
        forty_fifty[2]+=1
        if (row['Survived']==0):
            forty_fifty[0]+=1
        else:
            forty_fifty[1]+=1

    if ((row['Age']>50 and row['Age']<60)):
        fifty_sixty[2]+=1
        if (row['Survived']==0):
            fifty_sixty[0]+=1
        else:
            fifty_sixty[1]+=1

    if ((row['Age']>60 and row['Age']<70)):
        sixty_seventy[2]+=1
        if (row['Survived']==0):
            sixty_seventy[0]+=1
        else:
            sixty_seventy[1]+=1

print("")
print("age level survival information")
print("0~10:","Dead:",zero_ten[0],"Alive:",zero_ten[1],"total:",zero_ten[2],"dead ratio:",zero_ten[0]/zero_ten[2])
print("10~20:","Dead:",ten_twenty[0],"Alive:",ten_twenty[1],"total:",ten_twenty[2],"dead ratio:",ten_twenty[0]/ten_twenty[2])
print("20~30:","Dead:",twenty_thirty[0],"Alive:",twenty_thirty[1],"total:",twenty_thirty[2],"dead ratio:",twenty_thirty[0]/twenty_thirty[2])    
print("30~40:","Dead:",thirty_forty[0],"Alive:",thirty_forty[1],"total:",thirty_forty[2],"dead ratio:",thirty_forty[0]/thirty_forty[2])  
print("40~50:","Dead:",forty_fifty[0],"Alive:",forty_fifty[1],"total:",forty_fifty[2],"dead ratio:",forty_fifty[0]/forty_fifty[2]) 
print("50~60:","Dead:",fifty_sixty[0],"Alive:",fifty_sixty[1],"total:",fifty_sixty[2],"dead ratio:",fifty_sixty[0]/fifty_sixty[2]) 
print("60~70:","Dead:",sixty_seventy[0],"Alive:",sixty_seventy[1],"total:",sixty_seventy[2],"dead ratio:",sixty_seventy[0]/sixty_seventy[2]) 
#for index, row in train_df.iterrows():
#    if (pd.isnull(row['Age'])):
#        print(row['Name'])

class1_all=0
class2_all=0
class3_all=0

class1_dead=0
class2_dead=0
class3_dead=0

for index, row in train_df.iterrows():
    if (row['Pclass']==1):
        class1_all+=1
        if (row['Survived']==0):
            class1_dead+=1
    if (row['Pclass']==2):
        class2_all+=1
        if (row['Survived']==0):
            class2_dead+=1            
    if (row['Pclass']==3):
        class3_all+=1
        if (row['Survived']==0):
            class3_dead+=1

print("")
print("class level survival information:")
print("class 1 all:",class1_all,"class 1 dead:",class1_dead,"class 1 dead prob:",class1_dead/class1_all)
print("class 2 all:",class2_all,"class 2 dead:",class2_dead,"class 1 dead prob:",class2_dead/class2_all)
print("class 3 all:",class3_all,"class 3 dead:",class3_dead,"class 1 dead prob:",class3_dead/class3_all)

hassiball=0
hassibdead=0
nosiball=0
nosibdead=0
for index, row in train_df.iterrows():
    if (row['SibSp']>0):
        hassiball+=1
        if (row['Survived']==0):
            hassibdead+=1
    if (row['SibSp']>0):
        nosiball+=1
        if (row['Survived']==0):
            nosibdead+=1        
print("")
print("has siblings survival information")
print("has sib dead prob:",hassibdead/hassiball,"no sib dead prob",nosibdead/nosiball)
        

fromsall=0
fromcall=0
fromqall=0
fromsdead=0
fromcdead=0
fromqdead=0

for index, row in train_df.iterrows():
    if (row['Embarked']=='S'):
        fromsall+=1
        if (row['Survived']==0):
            fromsdead+=1
    if (row['Embarked']=='C'):
        fromcall+=1
        if (row['Survived']==0):
            fromcdead+=1            
    if (row['Embarked']=='Q'):
        fromqall+=1
        if (row['Survived']==0):
            fromqdead+=1

print("from S:",fromsall,"from S dead prob:",fromsdead/fromsall,"from Q:",fromqall,"from Q dead prob:",fromqdead/fromqall,"from C:",fromcall,"from C dead prob:",fromcdead/fromcall)

lowfareall=0
midfareall=0
highfareall=0
lowfaredead=0
midfaredead=0
highfaredead=0

for index, row in train_df.iterrows():
    if (row['Fare'] < 7.3):
        lowfareall+=1
        if (row['Survived']==0):
            lowfaredead+=1
    if (row['Fare'] > 7.3 and row['Fare']<=17):
        midfareall+=1
        if (row['Survived']==0):
            midfaredead+=1    
    if (row['Fare'] >= 18):
        highfareall+=1
        if (row['Survived']==0):
            highfaredead+=1    
print("")
print("amount of fare dead ratio")
print("low fare all:",lowfareall,"low fare dead:",lowfaredead/lowfareall,"mid fare all:",midfareall,"midfaredead:",midfaredead/midfareall,"high fare all:",highfareall,"high fare dead:",highfaredead/highfareall)






