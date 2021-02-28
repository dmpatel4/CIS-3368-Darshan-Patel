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
    userInput = input("Choose an option: \n")
    return userInput


if __name__ == "__main__":
    while True:
        userOption = print_menu()
        connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")

        if userOption == 'a':
            insertName = input("What is your Full Name? (ex: John Doe): ")
            phoneNumber = input("Insert Phone Number (ex: XXX-XXX-XXXX): ")
            dateCreated = date.today()
            insertQuery = "INSERT INTO contacts (fullName, contactDetails, creationDate) VALUES ('%s', '%s', '%s')" % (insertName, phoneNumber, dateCreated)
            execute_query(connection, insertQuery)

        elif userOption == 'd':
            userID = input("Insert userID to DELETE: ")
            deleteQuery = "DELETE FROM contacts WHERE id = %s" % userID
            execute_query(connection, deleteQuery)

        elif userOption == 'u':
            selectedName = input("Full Name of the user you would like to UPDATE: ")
            updatedContact = input("Insert updated Phone Number (ex: XXX-XXX-XXXX): ")
            updateQuery = """
            UPDATE contacts
            SET fullName = '%s'
            WHERE id = %s """ % (updatedContact, selectedName)
            execute_query(connection, updateQuery)

        elif userOption == 'b':
            selectContacts = """
            SELECT * FROM contacts
            ORDER BY contacts.fullName ASC """
            contacts = execute_read_query(connection, selectContacts)
            for contact in contacts:
                print(contact)

        elif userOption == 'c':
            selectContacts = """
            SELECT * FROM contacts
            ORDER BY contacts.creationDate ASC """
            contacts = execute_read_query(connection, selectContacts)
            for contact in contacts:
                print(contact)

        elif userOption == 'o':
            selectContacts = "SELECT * FROM contacts"
            contacts = execute_read_query(connection, selectContacts)
            for contact in contacts:
                print(contact)

        elif userOption == 'q':
            print("Thank You. Please visit us again.")
            exit()

        else:
            print("Sorry, please try again.")