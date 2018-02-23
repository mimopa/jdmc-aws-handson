# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:45:58 2018

@author: terauchi
"""

import numpy as np
import pandas as pd
import sklearn as sk

dataset = pd.read_csv('chiba.csv', encoding="cp932", header=1)
dataset1 = dataset.drop([2,3])
dataset2 = dataset1.drop(1)
city = dataset2.iloc[0]
clmlength = len(dataset2.columns)
#city = pd.DataFrame(dataset2.iloc[0])
city_length = (clmlength - 1) / 23



# 品質情報を含む列を取得
ds = dataset.T

#ds.drop(ds.index[ds[3] == '品質情報'],inplace = True)
#ds.drop(ds.index[ds[3] == '均質番号'],inplace = True)

# 元データとする
ds.drop(ds.index[ds[3] == '品質情報']|ds.index[ds[3] == '均質番号'],inplace = True)

# 気温だけ抜き出す
ds2 = ds[ds[1].str.contains('年月日時') | ds[1].str.contains("気温")]

ds3 = ds2.dropna(how='all', axis=1)
ds3.dropna(thresh=3, axis=0,inplace = True)
ds3.reset_index(drop=True, inplace=True)
# 数値だけに置き換えてみる
ds5 = ds3.drop(0)
ds5.reset_index(drop=True, inplace=True)
ds5.iloc[:,1:6]
#ds4 = ds3.T
#ds4[0].str.split('/', expand=True)

