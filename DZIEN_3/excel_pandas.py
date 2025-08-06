import pandas as pd
import xlsxwriter

df = pd.DataFrame({'Data':[10,12,34,24,66,34,23,5,33,125,245,765,456,889,543]})

writer = pd.ExcelWriter('pandas_dane.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='ramka')
writer._save()
