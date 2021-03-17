import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


file = open("results_pure.txt", 'r')
df = pd.DataFrame(index=range(0, 13), columns=range(0, 21))
df = df.fillna(0)

while True:
    line = file.readline()

    if not line:
        break

    info = line[:-1].split(" ")
    #
    # if np.isnan(df.loc[round(int(info[2]) / 100)][round(int(info[3]) / 100)]):
    #     print((np.isnan(df.loc[round(int(info[2]) / 100)][round(int(info[3]) / 100)])), '인데')
    #     df.loc[round(int(info[2]) / 100)][round(int(info[3]) / 100)] = 1

    df.loc[round(int(info[3]) / 100)][round(int(info[2]) / 100)] += 1
    # df = df.append(pd.DataFrame([[int(info[2]), int(info[3])]], columns=['x', 'y']))

file.close()

df = df.replace(0, np.nan)
df = df.reset_index(drop=True)

print(df)

# print(df)
# print(df['x'].max())
# print(df['x'].min())
# print(df['y'].max())
# print(df['y'].min())
# sns.heatmap(df, cmap="GnBu")

sns.heatmap(df, linewidths=0.1, linecolor="black")
plt.show()