#PYTHON MODULE: BOOK

from datetime import date
import os
import platform

import sqlite3

def clrscreen():
    if platform.system()=="windows":
        print(os.system("cls"))

def display():
    try:
        #os.system('cls')
        db = sqlite3.connect("library.db")
        query=("SELECT * FROM book")
        Cursor = db.execute(query)
        for(bno,bname,author,publisher,price,qty,d_o_purchase)in Cursor:
             print("=================================================")
             print("Book Code :",bno)
             print("Book Name :",bname)
             print("Author of Book :",author)
             print("Publisher:",publisher)
             print("Price of Book :",price)
             print("Total Quantity :",qty)
             print("Purchased on :",d_o_purchase)
             print("==================================================")
        db.close()
        #print("You have done it!!!!!!")
    except:
        print("Error (Book Display).")
    else:
        db.close()
    x=input("Enter any key to continue...")
        
def insertData():
    try:
        db = sqlite3.connect("library.db")
        bno=input("Enter Book Code :")                                     
        bname=input("Enter Book Name :")
        author=input("Enter Book Author's Name :")
        publisher=input("Enter Publisher of Book :")
        price=int(input("Enter Book Price :"))
        qty=int(input("Enter Quantity Purchased :"))
        print("Enter Date of Purchase(Date,Month and Year separately):")
        DD=int(input("Enter Date :"))
        MM=int(input("Enter Month :"))
        YY=int(input("Enter Year :"))
        Qry=("INSERT INTO book VALUES (?,?,?,?,?,?,?)")
        data=(bno,bname,author,publisher,price,qty,date(YY,MM,DD))
        db.execute(Qry,data)
        db.commit()
        db.close()
        print("Record Inserted Successfully.")
    except:
        print("Error(Book insert)")
        db.close()
    x=input("Enter any key to continue...")

def deleteBook():
    try:                                       
        db = sqlite3.connect("library.db")
        bno=input("Enter Book Code of Book to be deleted :")
        Qry=("DELETE FROM book WHERE bno= ?")
        del_rec=(bno,)
        db.execute(Qry,del_rec)
        db.commit()
        db.close()                                  
        print("Record(s) Deleted Successfully.")
    except:
        print("Error (Book Delete).")
        db.close()
    x=input("Enter any key to continue...")

def searchBookRec():
    try:
        db = sqlite3.connect("library.db")
        bno=input("Enter Book No to be Searched :")
        query=("SELECT * FROM book where bno=?")
        rec_srch=(bno,)
        Cursor = db.execute(query,rec_srch)
        rec_count=0
        for(bno,bname,author,publisher,price,qty,d_o_purchase) in Cursor:
           rec_count+=1
           print("=================================================")
           print("Book Code :",bno)
           print("Book Name :",bname)
           print("Author of Book :",author)
           print("Publisher :",publisher)
           print("Price of Book :",price)
           print("Total Quantity :",qty)
           print("Purchased on :",d_o_purchase)
           print("================================================")
           if rec_count%2==0:
               input("Press any key to continue")
               clrscreen()
        print(rec_count,"Record(s) found.")
        db.close()
    except:
        print("Error (Book Search).")
        db.close()
    x=input("Enter any key to continue...")

def updateBook():
    try:
        db = sqlite3.connect("library.db")
        bno=input("Enter Book Code of Book to be Updated :")                               
        rec_srch=(bno,)
        print("Enter New Data:")
        bname=input("Enter Book Name :")
        author=input("Enter Book Author's Name :")
        publisher=input("Enter Publisher of Book :")
        price=int(input("Enter Book Price :"))
        qty=int(input("Enter Quantity purchased :"))
        print("Enter Date of Purchase(Date,Month and Year seperately:")         
        DD=int(input("Enter Date :"))
        MM=int(input("Enter Month :"))          
        YY=int(input("Enter Year :"))
        Qry=("UPDATE book SET bname=?,author=?,publisher=?,price=?,qty=?,d_o_purchase=? WHERE bno=?")
        data=(bname,author,publisher,price,qty,date(YY,MM,DD),bno)
        db.execute(Qry,data)
        db.commit()
        db.close()
        print("Record(s) Updated Successfully.")
    except:
        print("Error (Book Update).")
        db.close()
    x=input("Enter any key to continue...")
