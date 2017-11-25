import pandas as pd


df = pd.read_csv('/home/qoo/Documents/ubike/自行車.csv')

print('各區可借與可還數量')
print(df.groupby('sarea')[['sbi', 'bemp']].sum())
print('-'*20)
print('總共可借數量', df['sbi'].sum())
print('總共可還數量', df['bemp'].sum())
print('-'*20)
print('各區站點個數統計')
print(df['sarea'].value_counts())