import pyodbc

server = '118.27.193.183,1433'
database = 'PatliteV2' 
username = 'sa' 
password = 'Hoplong6688' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

def get_connection():
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # print('Connection has been initial...')

        return cnxn
    except Exception as e:
        print('Connection error: ', e)
        return None

# get_connection()
