#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import dataframe as df

path = "C:/Windows/Fonts/Malgun.ttf"
fontprop = font_manager.FontProperties(fname=path, size=16).get_name()
# plt.rc('font', family=fontprop)
sns.set()

corona = pd.read_csv("D:/BigData/서울특별시 동작구_동별 코로나19 확진 및 완치 현황_20201020.csv", engine="python")
corona = corona.drop(corona.index[2])
print(corona)
dong = corona.plot(kind='bar', figsize=(12,6), fontsize=12)
dong.set_title('서울특별시 동작구 코로나 확진 및 완치 현황', fontproperties=fontprop)
dong.set_xlabel('구분',fontsize=12, fontproperties=fontprop)
dong.set_ylabel('확진/완치', fontsize=12, fontproperties=fontprop)
# dong.legend(['확진', '완치'], fontsize=12)

plt.legend()
plt.grid()

plt.show()
