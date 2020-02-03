import pandas as pd
def p(d):
    print(d)

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 30)

fileName = "C:\\Users\\gautap\\Desktop\\testdata\\weather_data_nan.csv"
df = pd.read_csv(fileName)
#p(df)
#p(type(df['day'][0]))

## Converted day column from string into date format.
df = pd.read_csv(fileName, parse_dates=['day'])
#p(df)
#p(type(df['day'][0]))

# fill any random value in place of NaN.
#newDF = df.fillna(0)
#p(newDF)

# fill values in place of NaN using specific values against specific columns
#newDF = df.fillna({
#    'temperature': 0,
#    'windspeed': 0,
#    'event': 'no event'
#})
#p(newDF)

# fill forward and backward values in place of NaN.
#newDF = df.fillna(method='ffill')
#p(newDF)
#newDF = df.fillna(method='bfill')
#p(newDF)

#newDF = df.dropna()
#p(newDF)

#newDF = df.dropna(how='all')
#p(newDF)

#newDF = df.dropna(thresh=3)
#p(newDF)

#newDF = df.interpolate()
#p(newDF)


########## REPLACE ##############
fileName = "C:\\Users\\gautap\\Desktop\\testdata\\weather_data_replace.csv"
df = pd.read_csv(fileName)
#p(df)

import numpy as np

#newDF = df.replace(-8888, np.NaN)
#p(newDF)

#newDF = newDF.replace([-9999, -7777], np.NaN)
#p(newDF)

#newDF = df.replace({
#    'temperature': [-8888, -7777, -9999],
#    'windspeed': -8888,
#    'event': 'No event'
#}, np.NaN)
#p(newDF)


#fileName = "C:\\Users\\gautap\\Desktop\\testdata\\weather_data_with_unit_replace.csv"
#df = pd.read_csv(fileName)
#p(df)
#newDF = df.replace('[A-Za-z]', np.NaN, regex=True)
#p(newDF)

#newDF = df.replace({
#    'temperature': '[A-Za-z]',
#    'windspeed': '[A-Za-z]'
#    }, '', regex=True)
#p(newDF)


studentDict = {
    'student': ['sachin', 'rakesh', 'rohit', 'anuja', "ram", 'abhi'],
    'grade': ['exceptional', 'average', 'good', 'poor', 'average', 'exceptional'],
}
testDF = pd.DataFrame(studentDict)
p(testDF)

newDF = testDF.replace(['exceptional', 'average', 'good', 'poor'], [3, 2, 1, 0])
p(newDF)