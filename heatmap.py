import pandas as pd
import matplotlib.pyplot as plt
import calendar
import seaborn as sns; sns.set_theme()

df = pd.read_csv('3131.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
df['M'] = df['datetime'].dt.month
df['Y'] = df['datetime'].dt.year
df.reset_index(drop=True, inplace=True)
df.set_index('datetime',inplace=True)

df_monthly = df.resample('M').last()
df_monthly['returns'] = (df_monthly['close']-df_monthly['close'].shift(1))*100/df_monthly['close'].shift(1)

heatmap_ret = pd.pivot_table(df_monthly,index='Y',columns='M',values=['returns'])
heatmap_ret.columns = [calendar.month_name[i] for i in range(1,13)]

plt.figure(figsize=(16,10))
ax = sns.heatmap(heatmap_ret, cmap='RdYlGn', annot=True)
ax.tick_params(top=True, labeltop=True)

ax.get_figure().savefig('heatmap.png')