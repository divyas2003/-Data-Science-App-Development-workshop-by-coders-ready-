# -*- coding: utf-8 -*-
"""ds workshop 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_pW8VzgQIfO44GmStlPVVwRXE8mXCABf
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import plotly.express as pr
import plotly.graph_objects as go

df = pd.read_csv('/content/project_dataset.csv (1)')

df

df1=df.copy()

df1.head(8 )

df.shape

df1.columns

df1.dtypes

df.info()

df1.describe()

df1.duplicated()

df1.isna()

df1.isna().sum()

df1.isna().sum()/df1.shape[0]

df1.dropna(axis=1, inplace=True)

df

df1.shape

data = df1.sample(n=500,random_state=42)

data

data.shape
data.columns
data.head()
data.tail

data.count()

