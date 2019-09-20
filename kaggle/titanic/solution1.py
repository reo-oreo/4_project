#データ分析と処理
import pandas as pd
import numpy as np
import random as rnd


#ビジュアル化
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

#機械学習
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import    DecisionTreeClassifier


#データの取得

train_df=pd.read_csv("./train.csv")
test_df=pd.read_csv("./test.csv")
combine=[train_df,test_df]

# sns.pairplot(train_df)
# plt.show()

#可視化によるデータの分析

#列名を表示させる
print(train_df.columns.values)

#データのプレビュー
print(train_df.head())

#infoを使って、欠損値をもつデータ項目と変数の種類を見分ける
print("■注意：418に満たない列名は欠損値を含まない、またデータ型がint,floatでない場合は質的変数とわかる")
train_df.info()
print('_'*40)
test_df.info()

print("---------")
#基本統計量の確認
print("■基本統計量をここで確認する")
print(train_df.describe())

#質的変数の確認
print("■質的変数の分布をここで確認する")
print(train_df.describe(include='O'))
print("-----"*10)
print(train_df.describe(include=np.number))

#データ分析に基づく推測
#相関、終了、修正、作成、分類


#特徴をピボットすることで分析

print("■PclassとSurvivedのピボット")
print(train_df[['Pclass','Survived']].groupby(['Pclass'],as_index=False).mean().sort_values(by='Survived',ascending=False))

print("■SexとSurvivedのピボット")
print(train_df[['Sex','Survived']].groupby(['Sex'],as_index=False).mean().sort_values(by='Survived',ascending=False))

print("■SibspとSurvivedのピボット")
print(train_df[['SibSp','Survived']].groupby(['SibSp'],as_index=False).mean().sort_values(by='Survived',ascending=False))

print("■ParchとSurvivedのピボット")
print(train_df[['Parch','Survived']].groupby(['Parch'],as_index=False).mean().sort_values(by='Survived',ascending=False))

#可視化によるデータ分析


#量的変数同士の相関
g=sns.FacetGrid(train_df,col='Survived')
g.map(plt.hist,'Age',bins=20)
plt.show()

#量的変数と順序変数の相関
grid=sns.FacetGrid(train_df,col='Survived',row='Pclass',height=2.2,aspect=1.6)
grid.map(plt.hist,'Age',alpha=.5,bins=20)
grid.add_legend()
plt.show()

#カテゴリー変数同士の相関
grid=sns.FacetGrid(train_df,row='Embarked',height=2.2,aspect=1.6)
grid.map(sns.pointplot,'Pclass','Survived','Sex',palette='deep')
grid.add_legend()
plt.show()
#カテゴリー変数と量的変数の相関
grid=sns.FacetGrid(train_df,row='Embarked',col='Survived',height=2.2,aspect=1.6)
grid.map(sns.barplot,'Sex','Fare',alpha=0.5,ci=None)
grid.add_legend()
plt.show()


#データ前処理


#特徴量の削除

print("Before",train_df.shape,test_df.shape,combine[0].shape,combine[1].shape)

train_df=train_df.drop(['Ticket','Cabin'],axis=1)
test_df=test_df.drop(['Ticket','Cabin'],axis=1)
combine=[train_df,test_df]

print("Adter",train_df.shape,test_df.shape,combine[0].shape,combine[1].shape)


#新たな特徴量の作成

for dataset in combine:
    dataset['Title']=dataset.Name.str.extract('([A-Za-z]+)¥.',expand=False)

print(pd.crosstab(train_df['Title'],train_df['Sex']))

for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

print(train_df[['Title', 'Survived']].groupby(['Title'], as_index=False).mean())


title_mapping={"Mr":1,"Miss":2,"Mrs":3,"Master":4,"Rare":5}

for dataset in combine:
    dataset['Title']=dataset['Title'].map(title_mapping)
    dataset['Title']=dataset['Title'].fillna(0)

print(train_df.head())

