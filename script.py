import sqlite3
# Import sqlite3 built-in library to interact with SQlite databases

def create_table():
    # Function to create a table in a database and add some data
    conn = sqlite3.connect("lite.db")
    # Establish the connection and store the connect method metod into conn
    # variable
    cur = conn.cursor()
    # Create a cursor object and store into cur variable
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # SQL query: in case there is no table called "store" then create it with
    # item, quantity and price columns whose data types are TEXT, INTEGER and
    # REAL respectively
    cur.execute("INSERT INTO store VALUES ('Wine Glass',8,10.5)")
    # Execute method to add new data into the store table following the
    # format previously defined for the columns
    conn.commit()
    # Commit the changes made
    conn.close()
    # Close the connection

def insert(item,quantity,price):
    # Function that takes as parameters the values that you pass to insert
    # them into "store" table
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    # (?,?,?) represents the variable that will substitued by the parameters
    # that are input in the insert function
    conn.commit()
    conn.close()

def view():
    # Function that selects data from the table, so it can be displayed
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # The excute methos selects all the data from "store" table
    rows = cur.fetchall()
    # The data selected is then fetched and stored into rows variable
    conn.close()
    return rows
    # The view function returns the rows variable, so when it is called by
    # print() it can be displayed

def delete(item):
    # Function that deletes data from the table
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    # The row is selected by defining the item value and then it is deleted
    # (item,) with its final comma is necessary to avoid error is sqlite3
    # library
    conn.commit()
    conn.close()

def update(quantity,price,item):
    # Function that updates existing data from the table
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
    (quantity,price,item))
    # Execute method updates quantity and price in the specified row that is
    # defined by item
    conn.commit()
    conn.close()

update(11,6,"Water Glass")
#delete("Wine Glass")
#insert("Coffe Cup",10,5)
print(view())
# Call of some the functions
