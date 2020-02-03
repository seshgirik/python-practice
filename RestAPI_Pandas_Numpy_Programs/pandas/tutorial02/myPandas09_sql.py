import pandas as pd
#import MySQLdb as m

import sqlalchemy as s

# READ data from SQL
# WRITE back data to SQL

def p(d):
    print(d)

p(pd.__version__)

def connectTODB():
    db = m.connect("db4free.net", "sql12250556", "Gale@123", "sql12250556")
    return db

def connectTODBUsingsqlalchem():
    db = s.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format("sql12250556",
                                                      "Gale@123",
                                                      "db4free.net",
                                                      "sql12250556"))
    return db

dbConn = connectTODBUsingsqlalchem()
sqlQuery = "Select * from Customers"
customerDF = pd.read_sql(sqlQuery, dbConn)

orderDF = pd.read_sql("Select * from Orders", dbConn)
p(customerDF)
p(orderDF)


newCustomerDict = {
    "Customers Name": ["vivek", "indu", "satish", "vijay"],
    "Phone Number": [123, 456, 789 , 1011],
    "id": [31, 32, 33, 34]
}
newDF = pd.DataFrame(newCustomerDict)
p(newDF)
newDF.rename(columns={
        "Customers Name": 'name',
        "Phone Number": 'phonenumber'
    },
    inplace=True
)

p(newDF)

newDF.to_sql(
    name="Customers",
    con=dbConn,
    index=False,
    if_exists="append"
)