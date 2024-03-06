#book_controller
import connect_to_db
import os
import book_model_1
from book_model_1 import Book, DatabaseHandler
import book_view_1
import db_conf

global table_name

def showAll():
    #gets list of all Book object
    param=db_conf.imp_config()
    print(param)
    db_handler = DatabaseHandler(host=param[0], user=param[1], password=param[2], database=param[3])

    conection = db_handler.connect()
    table_name='book'
    records = db_handler.browse_record(table_name)
    return records
    # for record  in records:
    #     print(record)
    # input("Naciśniej [ENETER]...")

def findBookbyTitle(): 
    #gets list of all Book that found
    answer=input("Enter book's title or extract: ")
    condition = "title LIKE '%"+answer+"%'"
    param=db_conf.imp_config()
    # print(param)
    db_handler = DatabaseHandler(host=param[0], user=param[1], password=param[2], database=param[3])

    conection = db_handler.connect()
    table_name='book'
    records = db_handler.findRecord(table_name, condition)
    if len(records)!=0:
        book_view_1.startView()
        book_view_1.showAllView(records)
        book_view_1.endView()
        # for record  in records:
        #     print(record)
    else:
        print("None of book's found")
    input("Naciśniej [ENETER]...")

    # db_handler.disconnect()
    return condition

def deleteBook(condition): 
    #gets list of all Book that found
    # answer=input("Enter book's title or extract to delete: ")
    
    choice = input("Do you want to delete records (y/n): ")
    if choice.lower()=='y':
        # condition = "title.lower().strip() like '%"+answer.lower().strip()+"%'"
        param=db_conf.imp_config()
        # print(param)
        db_handler = DatabaseHandler(host=param[0], user=param[1], password=param[2], database=param[3])

        # conection = db_handler.connect()
        table_name='book'
        db_handler.deleteRecord(table_name, condition)
        
        # print("Was/were deleted!", len(records), "record(s)")
        # for record  in records:
        #     print(record)
        # input("Naciśniej [ENETER]...")

def enterData():
    table_name='book'
    print("----------------------------------")
    print('GIVE DETAILS OF BOOK')
    print('----------------------------------')
    title = input("Give book's title:  ")
    author = input("Give author's name :  ")
    publisher = input("Give book's publisher:  ")
    year = input("Give year of book's release:  ")
    
    book = Book(title, author, publisher, year)
    return book

    

def insert_data_to_table(object, table_name):

    print(table_name)
    try:
    # Create a cursor object to execute SQL queries
        db=connect_to_db.db_connection()
        cursor = db.cursor()
        # print(cursor)
        # input("Naciśniej [ENETER]...")
        #Extract the attributes of the object
        attributes=vars(object)

        #Construct the INSERT query dynamically
        columns = ', '.join(attributes.keys())
        values_template = ', '.join(['%s'] * len(attributes))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_template})"
        #Execute the INSERT query
        cursor.execute(insert_query, tuple(attributes.values()))
        db.commit()
        db.close()

        input("Rekord zosstał zapisany, naciśnij [ENTER]...")
    except:
        print("WYSTĄPIŁ PROBLEM Z DODANIEM REKORDU DO BAZY")
        input("Naciśniej [ENETER]...")

def start():
    #MAIN MENU
    def menu():
        os.system('cls')
        print("""
        ===========================================
        HOME LIBRARY
        ===========================================
        1. Show all book from "Home library"
        2. Append new book
        3. Find book
        4. Delete book
        5. Quit
        ==========================================
        """)

        choice=input("Enter funkction and press ENTER:  ")
        return choice

    #OBŁUGA MENU
    choice=''
    while choice != '5':
        choice =menu()
        if choice == '1':
            os.system('cls')
            list=showAll()
            book_view_1.startView()
            book_view_1.showAllView(list)
            book_view_1.endView()
        if choice == '2':
            os.system('cls')
            table_name ='book'
            book=enterData()
            Book.addBook(book, table_name)
            input("Naciśnij [ENTER], aby powrócić do menu...")
        if choice == '3':
            os.system('cls')
            findBookbyTitle()
            # deleteBook()
            # print("FUNKCJA JESZCZE NIE DZIAŁA ..")
            input("Naciśnij [ENTER], aby powrócić do menu...")
        if choice == '4':
            os.system('cls')
            con=findBookbyTitle()
            deleteBook(con)
            # print("FUNKCJA JESZCZE NIE DZIAŁA ..")
            input("Naciśnij [ENTER], aby powrócić do menu...")
        # if choice == '5':
        #     os.system('cls')
        #     # export_dvds.ExportCSV()
        #     print("FUNKCJA JESZCZE NIE DZIAŁA ..")
        #     input("Naciśnij [ENTER], aby powrócić do menu...")
        # if choice == '6':
        #     os.system('cls')
        #     # import_csv.ImportCSV()
        #     print("FUNKCJA JESZCZE NIE DZIAŁA ..")
        #     input("Naciśnij [ENTER], aby powrócić do menu...")
        # if choice == '7':
        #     os.system('cls')
        #     # import_csv.ImportCSV()
        #     print("FUNKCJA JESZCZE NIE DZIAŁA ..")
        #     input("Naciśnij [ENTER], aby powrócić do menu...")
        # if choice == '8':
        #     os.system('cls')
        #     # import_csv.ImportCSV()
        #     print("FUNKCJA JESZCZE NIE DZIAŁA ..")
        #     input("Naciśnij [ENTER], aby powrócić do menu...")


    # answer=book_view.startView()
    # # answer = input("Shwo all position: [y/n]")
    # if answer == 'y':
    #     return showAll()
    # else:
    #     return book_view.endView()
    
if __name__ == "__main__":
    #running controller function
    start()
    