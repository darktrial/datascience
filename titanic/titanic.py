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
from sklearn.metrics import f1_score



origin_df = pd.read_csv('train.csv')
#test_df = pd.read_csv('test.csv')

train_df=origin_df[:600]
test_df=origin_df[600:]

#test_result=test_df["Survived"]
#dropping unnecesary fields

#handle training data
train_df=train_df.drop("SibSp",axis=1)
train_df=train_df.drop("Parch",axis=1)
train_df=train_df.drop("PassengerId",axis=1)
train_df=train_df.drop("Name",axis=1)
train_df=train_df.drop("Cabin",axis=1)
train_df=train_df.drop("Ticket",axis=1)
train_df=train_df[train_df.Age.notnull()]
train_df=train_df[train_df.Fare.notnull()]
train_df=train_df[train_df.Sex.notnull()]
train_df=train_df[train_df.Embarked.notnull()]
train_df=train_df[train_df.Pclass.notnull()]
train_result=train_df["Survived"]
train_df=train_df.drop("Survived",axis=1)
#print(train_df)
test_df=test_df.drop("SibSp",axis=1)
test_df=test_df.drop("Parch",axis=1)
test_df=test_df.drop("PassengerId",axis=1)
test_df=test_df.drop("Name",axis=1)
test_df=test_df.drop("Cabin",axis=1)
test_df=test_df.drop("Ticket",axis=1)
test_df=test_df[test_df.Age.notnull()]
test_df=test_df[test_df.Fare.notnull()]
test_df=test_df[test_df.Sex.notnull()]
test_df=test_df[test_df.Embarked.notnull()]
test_df=test_df[test_df.Pclass.notnull()]
test_result=test_df["Survived"]
test_df=test_df.drop("Survived",axis=1)


combine=[train_df]

for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map( {'male': 1, 'female': 2} ).astype(int)
    dataset.loc[ dataset['Age'] <= 20, 'Age'] = 1
    dataset.loc[(dataset['Age'] > 20) & (dataset['Age'] <= 50), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 50), 'Age'] = 3
    dataset.loc[ dataset['Fare'] < 7.3, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] >= 7.3) & (dataset['Fare'] <= 17), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 17), 'Fare'] = 2    
    dataset.loc[ dataset['Embarked'] == 'S', 'Embarked'] = 1
    dataset.loc[ dataset['Embarked'] == 'Q', 'Embarked'] = 2
    dataset.loc[ dataset['Embarked'] == 'C', 'Embarked'] = 3
dataset['Age'] = dataset['Age'].astype(int)
dataset['Fare'] = dataset['Fare'].astype(int)
print(train_df)


combine=[test_df]

for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map( {'male': 1, 'female': 2} ).astype(int)
    dataset.loc[ dataset['Age'] <= 20, 'Age'] = 1
    dataset.loc[(dataset['Age'] > 20) & (dataset['Age'] <= 50), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 50), 'Age'] = 3
    dataset.loc[ dataset['Fare'] < 7.3, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] >= 7.3) & (dataset['Fare'] <= 17), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 17), 'Fare'] = 2    
    dataset.loc[ dataset['Embarked'] == 'S', 'Embarked'] = 1
    dataset.loc[ dataset['Embarked'] == 'Q', 'Embarked'] = 2
    dataset.loc[ dataset['Embarked'] == 'C', 'Embarked'] = 3
dataset['Age'] = dataset['Age'].astype(int)
dataset['Fare'] = dataset['Fare'].astype(int)
print(test_df)

svc = SVC()
svc.fit(train_df, train_result)
y_pred=svc.predict(test_df)
print("SVC f1 score:",f1_score(test_result,y_pred,average="macro"))

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(train_df, train_result)
y_pred = knn.predict(test_df)
print("KNN f1 score:",f1_score(test_result,y_pred,average="macro"))

gaussian = GaussianNB()
gaussian.fit(train_df, train_result)
y_pred = gaussian.predict(test_df)
print("GussianNB f1 score:",f1_score(test_result,y_pred,average="macro"))

perceptron = Perceptron()
perceptron.fit(train_df, train_result)
y_pred = perceptron.predict(test_df)
print("Perception f1 score:",f1_score(test_result,y_pred,average="macro"))

decision_tree = DecisionTreeClassifier()
decision_tree.fit(train_df, train_result)
y_pred = decision_tree.predict(test_df)
print("Decision tree f1 score:",f1_score(test_result,y_pred,average="macro"))

random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(train_df, train_result)
y_pred = random_forest.predict(test_df)
print("random forest f1 score:",f1_score(test_result,y_pred,average="macro"))



#x_train=train_df["Sex"]
#x_train=x_train.reshape(len(x_train),1)


#x_result=train_df["Survived"]
#print(x_result.shape)

#svc = SVC()
#svc.fit(x_train, x_result)
#y_pred=svc.predict(x_train)
#print(y_pred)

#logreg = LogisticRegression()
#logreg.fit(x_train, x_result)
#Y_pred = logreg.predict(X_test)

#combine = [train_df, test_df]



