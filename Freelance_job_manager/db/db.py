import mysql.connector as connector


try:
    print("Establishing a new connection between MySQL and Python.")
    connection=connector.connect(user="root",password="POSTGRES")
    print("A connection between MySQL and Python is successfully established")

except connector.Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)


cursor = connection.cursor()


connection.database