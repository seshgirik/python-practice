import pandas as pd

# pip install pandas
# SERIES and DATAFRAME

def p(d):
    print(d)

l = ['humid', 'dry', 'rainy', 'sunny', 'cloudy']
climateSeries = pd.Series(l, name='event')
#p(type(climateSeries))
#p(climateSeries)
#p(dir(climateSeries))
#p("---- climateSeries.dtypes ----\n{}".format(climateSeries.dtypes))
#p("---- climateSeries.shape  ----\n{}".format(climateSeries.shape))
#p("---- climateSeries.head(n) ----\n{}".format(climateSeries.head(4)))
#p("---- climateSeries.tail(m) ----\n{}".format(climateSeries.tail(3)))



## Create DataFrame using csv file.
fileName = "C:\\Users\\gautap\\Desktop\\DesktopItems\\D2\\testdata\\weather_data.csv"
df = pd.read_csv(fileName)

p("---- Full data ----\n{}".format(df))
p("---- df.dtypes ----\n{}".format(df.dtypes))
p("---- df.shape  ----\n{}".format(df.shape))
p("---- df.head(5) ----\n{}".format(df.head(5)))
p("---- df.tail(3) ----\n{}".format(df.tail(3)))

'''
## Create DataFrame using Python dictionary object
weatherDict = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    'temperature': [32, 35, 28, 24, 31, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}
dictDataFrame = pd.DataFrame(weatherDict)
#p("---- Full data using dict ----\n{}".format(dictDataFrame))
#p("---- dictDataFrame.dtypes ----\n{}".format(dictDataFrame.dtypes))
#p("---- dictDataFrame.shape  ----\n{}".format(dictDataFrame.shape))
#p("---- dictDataFrame.head(5) ----\n{}".format(dictDataFrame.head(5)))
#p("---- dictDataFrame.tail(3) ----\n{}".format(dictDataFrame.tail(3)))


## Create DataFrame using Python List object
#dayList = ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017']
#dayListDataFrame = pd.DataFrame(dayList)
#p("---- Full data using list ----\n{}".format(dayListDataFrame))

## Create DataFrame using Python List of tuple object
#dataListTuple = [('1/1/2017',32, 6, 'Rain'),
#                 ('1/1/2017',30, 6, 'Snow'),
#                 ('1/1/2017',32, 6, 'Sunny'),
#                 ('1/1/2017',32, 6, 'Rain')]
#dataListTupleDF = pd.DataFrame(dataListTuple)
#p("---- Data using list of tuple with default column name ----\n{}".format(dataListTupleDF))

#dataListTupleDF = pd.DataFrame(dataListTuple, columns=['day', 'temperature', 'windspeed', 'event'])
#p("---- Data using list of tuple with custom column name ----\n{}".format(dataListTupleDF))

## Create DataFrame using Python List of dictionary object
#dataListDict = [{'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
#                 {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
#                 {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
#                 {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'}]
#dataListDictDF = pd.DataFrame(dataListDict)
#p("---- Data using list of dictionary ----\n{}".format(dataListDictDF))

## List columns
#p("---- List columns ----\n{}".format(df.columns))

## Get data from one column
#p("---- Get data from one column ----\n{}".format(df['day']))
#p("---- Get type of one column ----\n{}".format(type(df['day'])))

## Get data from specific columns
#p("---- Get data from specific columns ----\n{}".format(df[['day', 'temperature', 'event']]))

## Get data from DataFrame based on condition
#p("---- Get data where event is rain ----\n{}".format(df['event']== 'Rain'))
#newDF = df[(df['event']== 'Rain') & (df['temperature'] >20)]
#p("---- newDF ----\n{}".format(newDF))

## Get maximum temperature
#p("---- Get maximum temperature ----\n{}".format(df['temperature'].max()))
#p("---- Get minimum temperature ----\n{}".format(df['temperature'].min()))
#p("---- Get mean temperature ----\n{}".format(df['temperature'].mean()))
#p("---- Get standard deviation temperature ----\n{}".format(df['temperature'].std()))

## Get statistics of DataFrame
#p("---- df.describe ----\n{}".format(df.describe()))

## Set index
#newDF = df.set_index(df['day'])
#p("---- newDF with newIndex as day ----\n{}".format(newDF))
#newDF = df.set_index(df['day'], inplace=True)
#p("---- newDF with newIndex as day ----\n{}".format(newDF))
'''