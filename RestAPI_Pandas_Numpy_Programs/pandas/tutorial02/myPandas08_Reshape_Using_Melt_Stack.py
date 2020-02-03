import pandas as pd
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 30)

def p(d):
    print(d)

# Melt - used to transform or reshape data.
dict01 = {
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'mumbai': [23, 31, 11, 34, 14, 17, 16],
    'delhi': [13, 9, 10, 5, 17, 11, 61],
    'chennai': [33, 43, 11, 24, 41, 17, 21]
}

df01 = pd.DataFrame(dict01)
p(df01)

#help(pd.melt)
df02 = pd.melt(df01, id_vars=['day'], var_name='city', value_name='temperature')
p(df02)
'''
#p(df02[df02['city'] == 'mumbai'])
#p(df02[df02['city'] == 'delhi'])

# Stack - used to transpose innermost level of columns in a dataframe.
# Unstack - used to perform a reverse operation.

fileName = "C:\\Users\\gautap\\Desktop\\testdata\\dummy_stocks_2_level.xlsx"

df01 = pd.read_excel(fileName, header=[0,1])
p(df01)

df02 = df01.stack(level=0)
#p(df02)

df02 = df01.stack(level=1)
p(df02)
'''