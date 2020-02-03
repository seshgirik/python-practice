import numpy as np
import pandas as pd
def p(d):
    print(d)
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)

#fileName = "C:\\Users\\gautap\\Desktop\\testdata\\pokemon_data.csv"
#df = pd.read_csv(fileName)
#p(df)
#p(df.dtypes)
#p(df.head(5))
#p(df.tail(3))

## READ HEADERS
#p(df.columns)

## READ each column
#p(df['Name'])
#p(df['Name'][2:5])
#p(df[['Name','Type 1', 'HP']])
#p(df[['Name','Type 1', 'HP']][2:5])


## READ each row
#p(df.head(5))
#p(df.iloc[1])
#p(df.iloc[2:5])

#for index, row in df.iterrows():
#    print(index,row)

#p(df.loc[df['Type 1'] == "Fire"])
#p(df.loc[df['Type 1'] == "Grass"])


## READ specific location (using R & C)
#p(df.iloc[3, 4])

## Sorting/Describing Data
#p(df.describe())

#p(df.sort_values('Name', ascending=False))
#p(df.sort_values(['Type 1', 'HP']))
#p(df.sort_values(['Type 1', 'HP'], ascending=False).head(4))
#p(df.sort_values(['Type 1', 'HP'], ascending=[1,0]).head(4))
#p(df.sort_values(['Type 1', 'HP'], ascending=[0,1]).head(4))