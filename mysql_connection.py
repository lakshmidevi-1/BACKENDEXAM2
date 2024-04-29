import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='backend',
                                         user='root',
                                         password='root')

    # mySql_Create_Table_Query = """CREATE TABLE locations (
    #                              id INT,
    #                              location_id INT,
    #                              street_address VARCHAR(255),
    #                              postal_code INT,
    #                              city VARCHAR(255),
    #                              state_province VARCHAR(255),
    #                              country_id VARCHAR(255),
    #                              PRIMARY KEY (id, location_id)
    #                          ) """
    #
    query = """SELECT locations.location_id, locations.street_address, locations.city, locations.state_province, countries.country_name
               FROM locations
               JOIN countries ON locations.country_id = countries.country_id
               WHERE countries.country_name = 'Canada'"""

    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    if records:
        print("Address of Canada:")
        for record in records:
            print("Location ID:", record[0])
            print("Street Address:", record[1])
            print("City:", record[2])
            print("State/Province:", record[3])
            print("Country Name:", record[4])
            print()  # For spacing between records
    else:
        print("No address found for Canada.")

except mysql.connector.Error as error:
    print("Failed to fetch data from MySQL: {}".format(error))

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")