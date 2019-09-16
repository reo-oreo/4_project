
import pandas as pd

import numpy as np
#scikit-learnのインポート
from sklearn import tree


#trainとtestの読み込み

train=pd.read_csv('./train_2.csv')
test=pd.read_csv('./test_2.csv')


#trainの目的変数と説明変数の値を取得

target=train["Survived"].values
features_one=train[["Pclass","Sex","Age","Fare"]].values

#決定木の作成
my_tree_one=tree.DecisionTreeClassifier()
my_tree_one=my_tree_one.fit(features_one,target)


#testの説明変数の値を取得

test_features=test[["Pclass","Sex","Age","Fare"]].values

#testの説明変数を使って[my_tree_model]のモデルで予測

my_prediciton=my_tree_one.predict(test_features)

print(my_prediciton.shape)

#予測結果のCSV書き出し

#passengerIdの取得
PassengerId=np.array(test["PassengerId"]).astype(int)

#my_predictionとPassengerIdをデータフレームへ落とし込む
my_solution=pd.DataFrame(my_prediciton,PassengerId,columns=["Survived"])

#my_tree_one.csvとして書き出し
my_solution.to_csv("my_tree_one.csv",index_label=["PassengerId"])
