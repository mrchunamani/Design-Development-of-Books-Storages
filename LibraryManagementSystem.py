#Project on Library Management System
#------------------------------------------------------------------
#MAIN MODULE:LIBRARY MANAGEMENT

import MenuLib
import Book
import Issue

import sqlite3

# Creating or connecting to database
db = sqlite3.connect("library.db")

# Create book table
qry = '''CREATE TABLE IF NOT EXISTS book (
  bno text NOT NULL,
  bname text NOT NULL,
  author text NOT NULL,
  publisher text NOT NULL,
  price int NOT NULL,
  qty int NOT NULL,
  d_o_purchase date NOT NULL,
  PRIMARY KEY (bno)
)'''
db.execute( qry )

# Create issue table
qry = '''CREATE TABLE IF NOT EXISTS issue (
  bno text NOT NULL,
  mno text NOT NULL,
  d_o_issue date NOT NULL,
  d_o_return date
)'''
db.execute( qry )

# Create member table
qry = '''CREATE TABLE IF NOT EXISTS member (
  mno text NOT NULL,
  mname text NOT NULL,
  mmobile text NOT NULL,
  mdom date NOT NULL,
  address text NOT NULL,
  PRIMARY KEY (mno)
)'''
db.execute( qry )

# To show Main Menu of Library Management
while True:
    #Book.clrscreen()
    print("========================================================")
    print("\t\t Library Management")
    print("========================================================")
    print("1.Book Managemant")
    print("2.Members Managemant")
    print("3.Issue/Return Book")
    print("4.Exit")
    print("========================================================")
    choice=int(input("Enter Your Choice (1 to 4) :"))
    if  choice==1:
        MenuLib.menuBook()
    elif choice==2:
        MenuLib.menuMember()
    elif choice==3:
        MenuLib.menuIssueReturn()
    elif choice==4:
        break
    else:
        print("Wrong Choice.......Enter Your Choice Again")
    x=input("Enter any key to continue...")
