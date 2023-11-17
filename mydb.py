import mysql.connector

dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = 'acesso21!'

)

#preparar um cursor
cursorObject = dataBase.cursor()

#criando database
cursorObject.execute("CREATE DATABASE jueco")

print('All done!')