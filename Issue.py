# PYTHON MODULE : ROOMISSUE

from datetime import date
import os

import sqlite3

def clrscreen():
    print('\n' * 5)

def showIssuedRooms():
    try:
       #os.system('cls')
       db = sqlite3.connect("Hotelm.db")
       query=("SELECT R.rno,Class,M.mno,mname,d_o_roomissue,d_o_return FROM room R,roomissue I,member M where R.rno=I.rno and I.mno=M.mno and d_o_return is NULL")
       Cursor = db.execute(query)
       for(Rno,Class,Mno,Mname,doi,dor)in Cursor:
            print("========================================================")
            print("Room code :",Rno)
            print("Class :",Class)          
            print("Member code :",Mno)          
            print("Member Name :",Mname)          
            print("Date of roomissue :",doi)          
            print("Date of return :",dor)          
            print("========================================================")
       db.close()          
       #print("you have done it !")
    except:
       print("Error (Show Issue Rooms).")   
       db.close()
    x=input("Enter any key to continue...")

def issueRoom():
    try:
       db = sqlite3.connect("Hotelm.db")
       rno=input("Enter Room Code :")
       mno=input("Enter Member Code :")
       #print("Enter Date of Issue(Date,Month and Year separately):")
       #DD=int(input("Enter Date :"))
       #MM=int(input("Enter Month :"))                               
       #YY=int(input("Enter Year :"))
       issueDate=date.today()
       Qry=("INSERT INTO roomissue(rno,mno,d_o_roomissue) VALUES(?,?,?)")
       #data=(bno,mno,date(YY,MM,DD))
       data=(rno,mno,issueDate)
       db.execute(Qry,data)
       db.commit()                               
       db.close()
       print("Record Issued Successfully.")
    except:
       print("Error (Issue Room).")
       db.close()                                    
    x=input("Enter any key to continue...")

def returnRoom():
    try:
       db = sqlite3.connect("Hotelm.db")
       rno=input("Enter Room Code of Room to be Returned :")
       Mno=input("Enter Member Code of Member who is returning Room :") 
       retDate=date.today()
       Qry=("Update issue set d_o_return=? WHERE rno=? and mno=?")
       rec=(retDate,rno,Mno)
       db.execute(Qry,rec)
       db.commit()
       db.close()
       print("Room(s) Returned Successfully.")
    except:
       print("Error (Return Room).")
       db.close()
    x=input("Enter any key to continue...")

