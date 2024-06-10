from db_connection import create_connection, close_connection

def create_tables():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        with open('BDHabit/HabitScript.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        connection.commit()
        close_connection(connection)

if __name__ == "__main__":
    create_tables()