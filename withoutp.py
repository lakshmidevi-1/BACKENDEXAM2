import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='backend',
                                         user='root',
                                         password='root')

    # Query to fetch location details of Canada from the "locations" table
    location_query = """SELECT location_id, street_address, city, state_province, country_id
                        FROM locations
                        WHERE country_id = 'CA'"""

    cursor = connection.cursor()
    cursor.execute(location_query)
    location_records = cursor.fetchall()

    # Fetching country name from the "countries" table
    country_query = """SELECT country_name
                       FROM countries
                       WHERE country_id = 'CA'"""

    cursor.execute(country_query)
    country_record = cursor.fetchone()

    if location_records and country_record:
        print("Address of Canada:")
        for location_record in location_records:
            print("Location ID:", location_record[0])
            print("Street Address:", location_record[1])
            print("City:", location_record[2])
            print("State/Province:", location_record[3])
            print("Country Name:", country_record[0])
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
