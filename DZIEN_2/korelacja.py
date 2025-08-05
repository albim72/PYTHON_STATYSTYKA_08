import pandas as pd
from matplotlib import pyplot as plt

X = [1,2,3,4,5,6,7]
Y = [2,4,5,4,5,7,8]

df = pd.DataFrame({'X':X,'Y':Y})
print(df)

#scatter - punktowy
plt.scatter(df['X'],df['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot')
plt.show()

#korelacja
korelacja = df['X'].corr(df['Y'])
print(f"współczynnik korelacji: {korelacja}")
