import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursoe object of the database
cursor = connection.cursor()

# Q1 - select all records from the "Artist" Table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Aerosmith"])

# fetch the results (multiple)
# results = cursor.fetchall()

# fetch the result (single)
result = cursor.fetchone()

# close the connection
connection.close()

# print results
# for result in results:
print(result)
