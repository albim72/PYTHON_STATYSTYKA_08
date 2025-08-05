import matplotlib.pyplot as plt
import pandas as pd

#dane
dane = [1,2,3,4,5,6,7,8,9,10,85,25,8,24,94,234,112,3,90,32,6,93,63,82,68,21,11]

#histogram i wykres pudełkowe
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(dane,bins=10,color='skyblue',edgecolor='black')
plt.title("Histogram")
plt.subplot(1,2,2)
plt.boxplot(dane,vert=False)
plt.title("Boxplot")
plt.tight_layout()
plt.show()
