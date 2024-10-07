import mysql.connector
from mysql.connector import Error

from config import DB_HOST, DB_USER, DB_PASSWORD


def create_database_and_tables(cursor):
    with open("data_bases/creating_datas.sql", "r") as file:
        sql_script = file.read()
    try:
        for statement in sql_script.split(";"):
            if statement.strip():
                cursor.execute(statement)
        print("Database and tables created successfully.", "\n" * 2)
    except Error as e:
        print(f"Error: '{e}'")


def insert_sample_data(cursor):
    # Insert sample data into streets and houses tables
    cursor.execute("INSERT INTO streets (name, length) VALUES ('Main St', 5.2);")
    cursor.execute("INSERT INTO streets (name, length) VALUES ('Second St', 3.4);")
    cursor.execute("INSERT INTO streets (name, length) VALUES ('Third St', 2.1);")

    cursor.execute(
        "INSERT INTO houses (street_id, tenants, floors) VALUES (1, 300, 3);"
    )
    cursor.execute(
        "INSERT INTO houses (street_id, tenants, floors) VALUES (2, 200, 2);"
    )
    cursor.execute(
        "INSERT INTO houses (street_id, tenants, floors) VALUES (3, 100, 1);"
    )

    print("Sample data inserted.", "\n" * 2)


def sample_data(cursor):
    cursor.execute(
        """
        SELECT s.name, s.length, SUM(h.tenants) AS total_tenants
        FROM streets s
        LEFT JOIN houses h ON s.id = h.street_id
        GROUP BY s.id
        HAVING total_tenants < 500
        ORDER BY s.length DESC
        LIMIT 3;
    """
    )
    results = cursor.fetchall()
    print("Sampled data:", "\n")
    for row in results:
        print(row)
    print("\n" * 2)


def main():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
        )

        if connection.is_connected():
            cursor = connection.cursor()

            create_database_and_tables(cursor)
            cursor.execute("USE mydb;")
            insert_sample_data(cursor)
            connection.commit()
            sample_data(cursor)

    except Error as e:
        print(f"Error: '{e}'")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":
    main()
