from datetime import date
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def print_menu():
    print("\nMENU\n"
          "a - Add contact\n"
          "d - Remove contact\n"
          "u - Update contact details\n"
          "b - Output all contacts in alphabetical order\n"
          "c - Output all contacts by creation date\n"
          "o - Output all contacts\n"
          "q - Quit\n\n")


if __name__ == "__main__":
    print_menu()
    userOption = input("Choose an option: \n")
    connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")

    if userOption == 'a':
        phoneNumber = input("Insert Phone Number (ex: XXX-XXX-XXXX): ")
        dateCreated = date.today()
        insertQuery = "INSERT INTO contacts (contactDetails, creationDate) VALUES (phoneNumber, dateCreated)"
        execute_query(connection, insertQuery)
        print_menu()

    elif userOption == 'd':
        userID = input("Insert userID to DELETE: ")
        deleteQuery = "DELETE FROM contacts WHERE id = %s" % userID
        execute_query(connection, deleteQuery)
        print_menu()

    elif userOption == 'u':
        selectedID = input("Select userID to UPDATE: ")
        updatedContact = input("Insert updated Phone Number (ex: XXX-XXX-XXXX): ")
        updateQuery = """
        UPDATE contacts
        SET contactDetails = updatedContact
        WHERE id = selectedID"""
        execute_query(connection, updateQuery)
        print_menu()

    elif userOption == 'b':
        selectContacts = "SELECT * FROM contacts"
        # contacts = execute_read_query(connection, selectContacts)

    elif userOption == 'c':
        selectContacts = "SELECT * FROM contacts"
        # contacts = execute_read_query(connection, selectContacts)

    elif userOption == 'o':
        selectContacts = "SELECT * FROM contacts"
        contacts = execute_read_query(connection, selectContacts)
        print(contacts)
        print_menu()

    elif userOption == 'q':
        print("Thank You. Please visit us again.")

    else:
        print("Sorry, please try again.")
        print_menu()