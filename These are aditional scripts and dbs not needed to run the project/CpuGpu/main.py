import psycopg2


# Function to read data from the text file and populate the PostgreSQL database
def populate_database(file_path):
    # Database connection parameters
    db_params = {
        'host': 'localhost',
        'database': 'postgresDB',
        'user': 'postgres',
        'password': 'admin',
    }

    # Open the text file
    with open(file_path, 'r') as file:
        # Read lines from the file
        lines = file.readlines()

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    id = 0
    # Iterate through the lines and insert data into the database
    for i in range(0, len(lines), 4):
        manufacturer = lines[i+1].strip()
        model = lines[i + 2].strip()
        score = float(lines[i + 3].strip())
        id += 1
        # Insert data into the database without specifying the 'id' column
        cursor.execute(
            "INSERT INTO cpu_specs (id, manufacturer, model, score) VALUES (%s, %s, %s, %s)",
            (id, manufacturer, model, score)
        )

    # Commit the changes and close the connection
    connection.commit()
    connection.close()


# Specify the path to your text file
file_path = 'cpu_specs.txt'

# Call the function to populate the database
populate_database(file_path)
