import sqlite3

def clear_database():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('questions.db')
        c = conn.cursor()

        # Execute the DELETE SQL statement to clear all records from the table
        c.execute("DELETE FROM questions;")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("All records cleared from the database.")
    except sqlite3.Error as e:
        print("Error clearing the database:", e)

if __name__ == '__main__':
    clear_database()
