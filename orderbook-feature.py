import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Users\USER\seoyeon\2023-05-10-upbit-BTC-book.csv').apply(pd.to_numeric, errors='ignore')
df_trade = pd.read_csv(r'C:\Users\USER\seoyeon\2023-05-10-upbit-BTC-trade.csv').apply(pd.to_numeric, errors='ignore')

# 데이터는 24시간 데이터를 사용할 것임.
# 먼저 bid, ask를 나누어 두 개의 데이터프레임으로 feature를 계산할 것임.
df1 = df[df['type'] == 0]
df2 = df[df['type'] == 1]

# 의미 있는 feature를 만들기 위해서는 데이터의 중요한 변수들을 찾아 다듬어주고, 새로운 변수를 파생시켜야 함.
# 이를 위해서는 다양한 방법이 존재하는데, 트레이딩의 관점에서는 거래대금이 중요하다고 생각함.
# 단순 가격 혹은 체결량은 해당 호가에 대한 관심도를 대변하기에는 부족하기 때문임.
# 따라서 가격과 체결량을 곱한 거래대금(여기에서는 volume이라 표현)이 해당 호가에 대한 관심도를 보여주기에 적절하다고 생각함.
df1['volume'] = df1['price'] * df1['quantity']
df2['volume'] = df2['price'] * df2['quantity']

# 또한 기본적인 통계값으로 평균, 분산, 표준편차, 합, 중앙값을 계산함.
df1['mean'] = df1.mean(axis=1)
df1['var'] = df1.var(axis=1)
df1['std'] = df1.std(axis=1)
df1['sum'] = df1.sum(axis=1)
df1['median'] = df1.median(axis=1)
df2['mean'] = df2.mean(axis=1)
df2['var'] = df2.var(axis=1)
df2['std'] = df2.std(axis=1)
df2['sum'] = df2.sum(axis=1)
df2['median'] = df2.median(axis=1)

print(df1.head())
print(df2.head())

df1.to_csv('2023-05-10-bid-feature.csv')
df2.to_csv('2023-05-10-ask-feature.csv')


