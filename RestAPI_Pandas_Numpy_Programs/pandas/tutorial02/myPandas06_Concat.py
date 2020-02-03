import pandas as pd
def p(d):
    print(d)

northIndiaWeather = {
    'city': ['delhi', 'jaipur', 'shimla'],
    'temperature': [23, 31, 11],
    'humidity': [68, 81, 41]
}

southIndiaWeather = {
    'city': ['bangalore', 'chennai', 'pondicherry'],
    'temperature': [23, 39, 31],
    'humidity': [68, 91, 86]
}

dfNorthIndia = pd.DataFrame(northIndiaWeather)
p(dfNorthIndia)

dfSouthIndia = pd.DataFrame(southIndiaWeather)
p(dfSouthIndia)

indiaDF = pd.concat([dfNorthIndia, dfNorthIndia])
p(indiaDF)
print(indiaDF['city'])


indiaDF = pd.concat([dfNorthIndia, dfSouthIndia], ignore_index=True)
p(indiaDF)

indiaDF = pd.concat([dfNorthIndia, dfSouthIndia], keys=['northIndia', 'southIndia'])
p(indiaDF)


p(indiaDF.loc['northIndia'])
p(indiaDF.loc['southIndia'])

indiaDF = pd.concat([dfNorthIndia, dfSouthIndia])
p(indiaDF)

windspeedDict = {
    'city': ['delhi', 'jaipur', 'shimla'],
    'windspeed': [3, 7, 6],
}
windspeedDF = pd.DataFrame(windspeedDict)
indiaDF = pd.concat([dfNorthIndia, windspeedDF])
p(indiaDF)

indiaDF = pd.concat([dfNorthIndia, windspeedDF], axis=1)
p(indiaDF)


seriesObj = pd.Series(['humid', 'dry', 'rainy'], name='event')
newDF = pd.concat([dfNorthIndia, windspeedDF, seriesObj], axis=1)
p(newDF)
