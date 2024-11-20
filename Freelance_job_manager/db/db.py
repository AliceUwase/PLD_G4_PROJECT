import mysql.connector as connector


try:
    print("Establishing a new connection between MySQL and Python.")
    connection=connector.connect(user="root",password="POSTGRES")
    print("A connection between MySQL and Python is successfully established")

except connector.Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)


cursor = connection.cursor()


cursor.execute("DROP DATABASE IF EXISTS `freelance_job_manager`")
cursor.execute("CREATE DATABASE IF NOT EXISTS `freelance_job_manager`")
cursor.execute("SHOW DATABASES")
for database in cursor:
    print(database)

cursor.execute("USE `freelance_job_manager`")

connection.database