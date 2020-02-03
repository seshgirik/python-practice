import pandas as pd
def p(d):
    print(d)

dict01 = {
    'city': ['delhi', 'jaipur', 'shimla', 'mumbai'],
    'temperature': [23, 31, 11, 34]
}

dict02 = {
    'city': ['jaipur', 'delhi', 'bangalore', 'chennai'],
    'humidity': [68, 91, 86, 98]
}

df01 = pd.DataFrame(dict01)
df02 = pd.DataFrame(dict02)
p(df01)
p(df02)
# how
#   inner - intersection (default)
#   outer - union
#   left  - left join
#   right - right join
df03 = pd.merge(df01, df02, on='city')
p(df03)

df03 = pd.merge(df01, df02, on='city', how='inner')
p(df03)

df03 = pd.merge(df01, df02, on='city', how='outer')
p(df03)

df03 = pd.merge(df01, df02, on='city', how='left')
p(df03)

df03 = pd.merge(df01, df02, on='city', how='right')
p(df03)


# indicator - tells us that data is coming from which side of DF ( left or join or both).
df03 = pd.merge(df01, df02, on='city', how='outer', indicator=True)
p(df03)

'''
# suffixes - append default values '_x' and '_y' for common columns from two or more dataframes.
dict01 = {
    'city': ['delhi', 'jaipur', 'shimla', 'mumbai'],
    'temperature': [23, 31, 11, 34],
    'windspeed': [7, 3, 4, 2]           # common columns
}

dict02 = {
    'city': ['jaipur', 'delhi', 'bangalore', 'chennai'],
    'humidity': [68, 91, 86, 98],
    'windspeed': [8, 13, 24, 12]
}

df01 = pd.DataFrame(dict01)
df02 = pd.DataFrame(dict02)

df03 = pd.merge(df01, df02, on='city', how='outer', indicator=True)
p(df03)
'''