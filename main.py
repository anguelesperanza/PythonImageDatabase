from PIL import Image
import sqlite3
import os

conn = sqlite3.connect('cards.db')

def make_table():        
    print("Opened database successfully")
    # Creates a table in the database called CARDS
    conn.execute('''
    CREATE TABLE CARDS  
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    URL TEXT NOT NULL); 
    ''')
    print("Table created succesfully")

def get_cards():
    return os.listdir(r'Cards')

def insert_cards(cl):
    i = 00000
    for c in cl:
        conn.execute(f'INSERT INTO CARDS VALUES ({i}, "{c}", "Cards/{c}")')
        i += 1
    conn.commit()

def show_images():

    for image in conn.execute('SELECT URL FROM CARDS'):
        im = Image.open(image[0])
        im.show()


def main():
    cards_list = get_cards()
    # insert_cards(cards_list)
    show_images()
    conn.close()
if __name__=="__main__":
    main()

