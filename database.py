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
<<<<<<< HEAD
        print('Connection has been initial...')
=======
        # print('Connection has been initial...')
>>>>>>> b90a14cf475b1f428c9da3d7fd6e0579cba7fc96

        return cnxn
    except Exception as e:
        print('Connection error: ', e)
        return None

<<<<<<< HEAD
get_connection()
=======
# get_connection()
>>>>>>> b90a14cf475b1f428c9da3d7fd6e0579cba7fc96
