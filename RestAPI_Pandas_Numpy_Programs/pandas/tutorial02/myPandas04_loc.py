import pandas as pd
def p(d):
    print(d)

fileName = "C:\\Users\\gautap\\Desktop\\testdata\\pokemon_data.csv"
df = pd.read_csv(fileName)
#p(df.head(5))
#p(df.tail(3))

## Filtering Data ##
#r = df.loc[df['Type 1'] == "Grass"]
#p(r)

#r = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison")]
#p(r)

#r = df.loc[(df['Type 1'] == "Grass") | (df['Type 2'] == "Poison")]
#p(r)

#newDF = df.loc[((df['Type 1'] == "Grass") | (df['Type 2'] == "Poison")) & (df['Speed'] < 40)]
#p(newDF)
#newDF.to_csv('C:\\Users\\gautap\\Desktop\\testdata\\filtered_data.csv')
#p(newDF.head(5))
#anotherDF = newDF.reset_index(drop=True)
#p(anotherDF.head(5))

#newDF = df.loc[df['Name'].str.contains('Mega')]
#p(newDF.head(6))

#newDF = df.loc[~df['Name'].str.contains('Mega')]
#p(newDF.head(6))

## Conditional changes into Data Frame ##
#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'Some random changes.'
#p(df)

#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['testGeneration', 'testLegendary']
#p(df)

## Aggregate Group by ##
df.groupby(['Type 1']).count()
p(df.head(100))