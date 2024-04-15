import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inFilename = '/Users/bummy/Documents/pythontest/source/Excel/singer.xlsx'
outFilename = '/Users/bummy/Documents/pythontest/source/Excel/singer_youtube'

df_senior = pd.read_excel(inFilename, 'senior', index_col=None)
df_junior = pd.read_excel(inFilename, 'junior', index_col=None)

df_singer = pd.concat( [df_senior, df_junior])
df_singer_youtube = df_singer[df_singer['인원'] >= 4]
df_singer_youtube = df_singer_youtube.sort_values(by=['인원'], axis=0, ascending=False)
df_singer_youtube = df_singer_youtube.loc[:, ['아이디', '이름', '인원', '유튜브 조회수']]

x_data = df_singer_youtube['아이디']
y_data = df_singer_youtube['인원']
colorAry = [np.random.choice(['red', 'blue', 'green', 'browm', 'orange', 'purple', 'gold', '']) for _ in range(len(x_data)) ]
SizeAry = np.sqrt(x_data**2 + y_data**2)

plt.scatter(x_data, y_data, s=SizeAry, c=colorAry)
plt.colorbar()
plt.show()
