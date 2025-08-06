import pandas as pd
import xlsxwriter

df = pd.DataFrame({
    'Kraj':['Chiny','Indie','USA','Indonezja'],
    'Populacja':[1_404_338_840,1_366_938_189,330_267_997,269_603_400],
    'Pozycja':[1,2,3,4]
})

df = df[['Pozycja','Kraj','Populacja']]
print(df)

writer = pd.ExcelWriter('populacja_world.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='pop',startrow=1,header=False,index=False)

workbook = writer.book
worksheet = writer.sheets['pop']
(max_row,max_col) = df.shape
column_settings = [{'header':column} for column in df.columns]

worksheet.add_table(0,0,max_row,max_col-1, {'columns':column_settings})
worksheet.set_column(0,max_col-1,12)

writer._save()
