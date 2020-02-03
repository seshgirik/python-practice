import pandas as pd
def p(d):
    print(d)

fileName = "C:\\Users\\gautap\\Desktop\\DesktopItems\D2\\testdata\\weather_data_grpby.csv"
df = pd.read_csv(fileName)
p(df)

df01 = df.groupby('city')
p(df01)

for city, city_df in df01:
    print(city, "\n", city_df)

#p(df01.get_group('mumbai'))
#p(df01.get_group('delhi'))
#p(df01.get_group('bangalore'))
#p(df01.get_group('chennai'))

#p(df01.max())
#p(df01.mean())
#p(df01.median())
#p(df01.std())
#p(df01.min())
#p(df01.describe())