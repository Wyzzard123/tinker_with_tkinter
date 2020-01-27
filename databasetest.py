from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')
root.geometry("400x400")


# Databases


# Create a database or connect to one
conn = sqlite3.connect('address_book.db') # If this database does not exist, this command will create it for us and save it in the current directory

# Create cursor
c = conn.cursor()

# Commenting out as table has been created
'''
# Create table
c.execute("""CREATE TABLE addresses (
    first_name text, 
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''

# Create function to delete a record
def delete():
    # Connect to database
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    # Delete a record
    c.execute(f"DELETE from addresses WHERE oid={delete_box.get()}")


    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

def submit():
    
    # Connect to database
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",  
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode':zipcode.get()
    })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function
def query():
    
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() # You can also fetchone or fetchmany(<number of records>)
    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += f"{record[0].rstrip()} {record[1].rstrip()}\t {record[-1]}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
    
    return

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0)) # Tuple in pady is for padding above and below

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0, pady=5) 

# Create submit button
submit_button = Button(root, text="Add Record to Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a delete button
delete_button = Button(root, text="Delete Records", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

root.mainloop()