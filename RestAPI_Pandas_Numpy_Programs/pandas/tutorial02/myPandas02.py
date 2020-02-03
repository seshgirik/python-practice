import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 30)

def p(d):
    print(d)

fileName = "C:\\Users\\gautap\\Desktop\\DesktopItems\\D2\\testdata\\pokemon_data.csv"
df = pd.read_csv(fileName)
#p(df.info())
#p(df.head(5))
p(df.tail(3))


## Making changes to Data
#p(df.head(5))

# One way
#df['myTotal'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
#p(df.head(5))

# slicing
# Another way
#p(df.iloc[2:7, 5:11])
#df['myTotal'] = df.iloc[2:7, 5:11].sum(axis=1)
#p("THIS IS USING iloc() \n{}".format(df.head(10)))


## Moving column
columnList = list(df.columns)
#df = df[columnList[0:4] + [columnList[-1]] + columnList[4:12]]
#df = df[columnList[0:4] + [columnList[-1]]]
#p(df.head(5))


## Drop column from df.
newDF = df.drop(columns=['Total'])
p(newDF.head(5))
p(df.head(5))
'''
#newCSV = "C:\\Users\\gautap\\Desktop\\testdata\\modified_data.csv"
#df.to_csv(newCSV)
'''
