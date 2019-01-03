# use Python 3.7.0 64-bit ('base':conda) environment
import pandas as pd, pandas.io.sql, pyodbc

# Parameters
driver = '{ODBC Driver 13 for SQL Server}'
server = 'EXAMPLE'
db = 'SUPER_SECRET_DATA'
uid = ''
pwd = ''

# connection String
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + 
    db + ';Trusted_Connection=yes;')

# Query
sql = '''

select top 100 *
from ALL_THE_PLACES

'''

# Create dataframe
df = pd.read_sql(sql,conn)

# Print data
print(df)
