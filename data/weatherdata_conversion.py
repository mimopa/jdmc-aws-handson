# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:45:58 2018

@author: terauchi
"""

import numpy as np
import pandas as pd
import sklearn as sk
from sklearn import preprocessing

# csvを読み込んだ時点で、見出し等も決めておく
# index=都市の数
# columns=都市ID（文字列→数値に変換）,項目ID（気温、雨量、など色々文字列→数値に変換）,2017/12/01 1:00から1時間ごとに2018/02/20 0:00まで1943列
dataset = pd.read_csv('chiba.csv', encoding="cp932", header=1)
dataset1 = dataset.drop([2,3])
dataset2 = dataset1.drop(1)
# 品質情報を含む列を取得
ds = dataset.T
# 元データとする
ds.drop(ds.index[ds[3] == '品質情報']|ds.index[ds[3] == '均質番号']|ds.index[ds[3] == '現象なし情報'],inplace = True)
# 気温だけ抜き出す
ds2 = ds[ds[1].str.contains('年月日時') | ds[1].str.contains("気温") | ds[1].str.contains("降水量") | ds[1].str.contains("降雪") | ds[1].str.contains("風速")]

# NaNを消す
ds3 = ds2.dropna(how='all', axis=1)
ds3.dropna(thresh=3, axis=0,inplace = True)
ds3.reset_index(drop=True, inplace=True)

ds4 = ds3.drop(2,axis=1)
ds4.drop(ds4.index[ds4[0] == "東庄"]|ds4.index[ds4[0] == "鋸南"]|ds4.index[ds4[0] == "大多喜"],inplace = True)

#ds5 = ds4.drop(ds4[0] == "東庄"|ds4[0] == "鋸南"|ds4[0] == "大多喜")
ds5 = ds4.T
ds5['City'] = pd.Series( '香取', index=ds5.index )
ds6 = ds5.T

# 気温、降水量、風速、風向き

# ↓はテスト用

# calumnをリネームする
ds3.columns = ['City','Type','2017/12/01 1:00','2017/12/01 2:00','2017/12/01 3:00','2017/12/01 4:00',]

# 数値だけに置き換えてみる
ds5 = ds3.drop(0)
ds5.reset_index(drop=True, inplace=True)
# カラムから抜き出すテスト
ds5.iloc[:,1:6]
ds3[0:1]
ds3[0:1][4]

# カラム名を変更するテスト：一括ではむずかしいが、日付を全部いれるのは。。。微妙
ds4 = ds3.iloc[:,0:4]
ds4.columns = ['City','Type','2017/12/01 1:00','2017/12/01 2:00']
# 見出しに移した行を削除
ds4.iloc[1:,0:4]
ds6 = ds4.iloc[1:,0:4]
# lambdaで処理できるなら、文字列を作るループを入れ込めばできるかも？
# df_new = df.rename(columns=lambda s: s.upper(), index=lambda s: s.lower())

# 文字列データを数値化
le = preprocessing.LabelEncoder()
le.fit_transform(ds6['City'])

for col in ds6.columns:
    if (ds6[col].dtypes == int) or (ds6[col].dtype == float):
        pass
    else:
        ds6[col] = le.fit_transform(ds6[col])


# 項目値の「気温」などをラベルエンコーディングする
# http://qs.nndo.jp/2017/09/15/838/

