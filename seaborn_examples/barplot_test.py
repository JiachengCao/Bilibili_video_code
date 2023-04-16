import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 1 加载数据
# 链接: https://gitee.com/nicedouble/seaborn-data/
#penguins = pd.read_csv(r'https://gitee.com/nicedouble/seaborn-data/raw/master/penguins.csv')
penguins = pd.read_csv(r'C:/Users/Administrator/Downloads/seaborn-data-master/seaborn-data-master/penguins.csv')
penguins = penguins.head(10) # 默认返回前5行
print(penguins)

# 2 设置图样式
#plt.figure(figsize=[20, 15], dpi=300) # 图形分辨率, dpi 值越大图片越清晰
plt.rcParams['figure.dpi'] = 100
sns.set_theme(style='darkgrid')   # 黑色背景，白色网格线
#sns.set_theme(style='whitegrid')   # 白色背景，黑色网格线

# 3 绘制图
ax = sns.barplot(data=penguins, x="species1", y="bill_length_mm", width=0.6)
#hue="sex"

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=20)
# 4 显示图形并保存
plt.show()

fig = ax.get_figure()
# 直接savefig时显示不全
fig.savefig('withoutTight.png')
# savefig时加上 bbox_inches='tight' 后，可以解决
fig.savefig('tight.png', bbox_inches='tight')