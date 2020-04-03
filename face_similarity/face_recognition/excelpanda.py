import pandas as pd

#读取哪几列
columns=['姓名','失效时间']

#源文件地址
file_loc = "C:\\Users\\fang\\Desktop\\source.xlsx"
df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols = columns)

#此处可以对df进行数据过滤筛选

print(df)

#新excel的列名
data_df = pd.DataFrame(df)
data_df.columns = columns

#新文件存储到哪里
writer = pd.ExcelWriter('C:\\Users\\fang\\Desktop\\des.xlsx')
data_df.to_excel(writer,float_format='%.5f')
writer.save()
