import numpy as np
import pandas as pd

#学習データと検証データ
train=pd.read_csv('./train.csv')
test=pd.read_csv('./test.csv')

print(train.shape)
print(test.shape)

#内容を概査
print(test.head())
print(train.head())

#基本統計量の確認
print(test.describe())
print(train.describe())


def kesson_table(df):
    null_val = df.isnull().sum()
    percent = 100 * df.isnull().sum() / len(df)
    kesson_table = pd.concat([null_val, percent], axis=1)
    kesson_table_ren_columns = kesson_table.rename(
        columns={0: '欠損数', 1: '%'})
    return kesson_table_ren_columns


print(kesson_table(train))
print(kesson_table(test))


##trainデータセットの事前処理


#欠損値対応

train["Age"]=train["Age"].fillna(train["Age"].median())
train["Embarked"]=train["Embarked"].fillna("S")

print(kesson_table(train))

#文字列の数字変換

train.Sex=train.Sex.replace("male",0)
train.Sex=train.Sex.replace("female",1)

train.Embarked=train.Embarked.replace("S",0)
train.Embarked=train.Embarked.replace("C",1)
train.Embarked=train.Embarked.replace("Q",2)

# train[train["Sex"]=="male"]=0
# train[train["Sex"]=="female"]=1
# train[train["Embarked"]=="S"]=0
# train[train["Embarked"]=="C"]=1
# train[train["Embarked"]=="Q"]=2

print(train.head(10))

##testデータセットの事前処理

test["Age"]=test["Age"].fillna(test["Age"].median())

test.Sex=test.Sex.replace("male",0)
test.Sex=test.Sex.replace("female",1)

test.Embarked=test.Embarked.replace("S",0)
test.Embarked=test.Embarked.replace("C",1)
test.Embarked=test.Embarked.replace("Q",2)
test["Fare"]=test["Fare"].fillna(test["Fare"].median())


print(kesson_table(test))


test.to_csv('./test_2.csv')
train.to_csv('./train_2.csv')


