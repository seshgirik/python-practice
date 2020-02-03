import pandas as pd
def p(d):
    print(d)

fileName = "C:\\Users\\gautap\\Desktop\\testdata\\pokemon_data.csv"
df = pd.read_csv(fileName)
#p(df.head(5))
#p(df.tail(3))

## Making changes to Data
#p(df.head(5))

# One way
#df['myTotal'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
#p(df.head(5))

# Another way
#df['myTotal'] = df.iloc[:, 5:11].sum(axis=1)
#p(df.head(5))


## Moving column
#columnList = list(df.columns)
#df = df[columnList[0:4] + [columnList[-1]] + columnList[4:12]]
#p(df.head(5))

## Drop column from df.
#newDF = df.drop(columns=['Total'])
#p(newDF.head(5))

#newCSV = "C:\\Users\\gautap\\Desktop\\testdata\\modified_data.csv"
#df.to_csv(newCSV)

