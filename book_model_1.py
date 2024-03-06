#book_model
import json
import mysql.connector
import connect_to_db

# class Author(object):
#     def __init__(self, id, fname, sname):
#         self.id = id
#         self.fname = fname
#         self.sname = sname
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

class Book():
    def __init__(self, title, author,publisher, year ):
        # self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
    #returns book title, author, publisher, year
    
    # def set_author(self, author):
    #     self.author = author

    def __str__(self):
        return 'Book( title -'+ self.title+'\n author(s) - '+self.author +'\n publisher - '+self.publisher+'\n year - '+self.year+')'

    # def position(self):
    #     return ("%s %s" % (self.title, self.author))

    @classmethod
    #returns all books inside db as list of Book object
    def getAll(self):
        with open('c:/Python_projects/New_projects/Next_MVC/Books/db.txt', 'r') as database:
        # print(database)
            result = []
            data_list =[]
            # json_list = json.loads(database)
            for line in database:
                data_list.append(json.loads(line))
            print(data_list)
            for item in data_list:
                book = Book(item['title'], item['author'], item['publisher'], item['year'])
                result.append(book)
        return result
       
    @classmethod
    # def addBook(self, list):
    def addBook(self, object, table_name):
        db=connect_to_db.db_connection()
        cursor = db.cursor()
        # print(cursor)
        attributes=vars(object)
        for item in attributes:
            print(item)
        #Construct the INSERT query dynamically
        columns = ', '.join(attributes.keys())
        values_template = ', '.join(['%s'] * len(attributes))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_template})"
        # print(tuple(attributes.values()))
        #Execute the INSERT query
        cursor.execute(insert_query, tuple(attributes.values()))
        db.commit()
        db.close()

class DatabaseHandler():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            conn = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
            )
            conn=connect_to_db.db_connection()
            cursor = conn.cursor()
            print("Connected to MySQL database")
        except mysql.connector.Error as err:
            print("Erroe:", err)
        return cursor

    def browse_record(self, table_name):

        conn=connect_to_db.db_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        conn.close()
        return records
    
    def findRecord(self, table, condition):
        conn=connect_to_db.db_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM {table} WHERE {condition}"
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return records
        
    
    def deleteRecord(self, table, condition):
        conn=connect_to_db.db_connection()
        cursor = conn.cursor()
        print(condition)
        query = f"DELETE FROM {table} WHERE {condition}"
        cursor.execute(query)
        conn.commit()
        cursor.close()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from MySQL database")
