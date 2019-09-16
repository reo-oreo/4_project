
import pandas as pd

import numpy as np
#scikit-learnのインポート
from sklearn import tree


#trainとtestの読み込み

train=pd.read_csv('./train_2.csv')
test=pd.read_csv('./test_2.csv')


#trainの目的変数と説明変数の値を取得

target=train["Survived"].values
features_two=train[["Pclass","Sex","Age","Fare","SibSp","Parch","Embarked"]].values

#決定木の作成と引数の設定
max_depth=10
min_samples_split=5
my_tree_two=tree.DecisionTreeClassifier(max_depth=max_depth,min_samples_split=min_samples_split)
my_tree_two=my_tree_two.fit(features_two,target)


#testの説明変数の値を取得

test_features=test[["Pclass","Sex","Age","Fare","SibSp","Parch","Embarked"]].values

#testの説明変数を使って[my_tree_model]のモデルで予測

my_prediciton_two=my_tree_two.predict(test_features)

print(my_prediciton_two.shape)

#予測結果のCSV書き出し

#passengerIdの取得
PassengerId=np.array(test["PassengerId"]).astype(int)

#my_predictionとPassengerIdをデータフレームへ落とし込む
my_solution_tree_two=pd.DataFrame(my_prediciton_two,PassengerId,columns=["Survived"])

#my_tree_one.csvとして書き出し
my_solution_tree_two.to_csv("my_tree_two.csv",index_label=["PassengerId"])
