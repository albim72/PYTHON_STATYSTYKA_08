import pandas as pd
import xlsxwriter


df = pd.DataFrame({
    'Miesiąc':[1,2,3,4,5,6,7,8,9,10,11,12],
    'Wartość sprzedaży':[2340,1340,2002,1700,6700,5500,1200,1780,2300,2500,1230,1000],
    'Procent':[.47,.24,.321,.43,.243,1.1356,.2,.67,.09,.54,.21,.28]
})

print(df)

writer = pd.ExcelWriter('procenty.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='proc',index=False)


workbook = writer.book
worksheet = writer.sheets['proc']

format1 = workbook.add_format({'num_format':'#.##00'})
format2 = workbook.add_format({'num_format':'0.0%'})

worksheet.set_column(2,1,22,format1)
worksheet.set_column(3,2,None,format2)

writer._save()
