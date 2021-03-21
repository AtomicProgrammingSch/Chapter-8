import sqlite3

connection = sqlite3.connect("./Library.db")  # I dislike their variable name!!!
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Books (
book_isbn text,
book_title text,
book_type text,
book_author text,
publisher text
)""")
# IF NOT EXISTS ensures no exception is thrown if the table already exists *cough* *cough* running this program twice

cursor.execute(f"""INSERT INTO Books (book_isbn, book_title, book_type, book_author, publisher) VALUES 
("978-0-340-88851-3", "A2 Pure Mathematics", "Non fictional", "Catherine Berry", "Hodder Education")""")

cursor.execute("""INSERT INTO Books (book_isbn, book_title, book_type, book_author, publisher) VALUES 
("978-1-118-10227-5", "Android 4 Application Development", "Non fictional", "Reto Meiser", "Wiley")""")

cursor.execute("""INSERT INTO Books (book_isbn, book_title, book_type, book_author, publisher) VALUES 
("0-596-00699-3", "Programming C#", "Non fictional", "Jesse Liberty", "O Reilly")""")


cursor.execute("SELECT * FROM books")
book_dictionary = cursor.fetchall()
for book in book_dictionary:
    print(book)
cursor.close()
connection.close()
