#PYTHON MODULE: MEMBER

from datetime import date
import os
import sqlite3

def clrscreen():
    print('\n' *5)
                                         
def display():
    try:
       #os.system('cls')                               
       db = sqlite3.connect("library.db")
       query=(" SELECT * FROM member")
       Cursor = db.execute(query)
       for(mno,mname,mmobile,mdom,address)in Cursor:
            print("========================================================")
            print("Member Code :",mno)
            print("Member Name :",mname)          
            print("Mobile No. of Member :",mmobile) 
            print("Date of Membership :",mdom)
            print("Address :",address) 
            print("========================================================")
       db.close()                              
       # print("You have done it !")                          
    except:
       print("Error (Display Members).")
       db.close()
    x=input("Enter any key to continue...")

def insertMember():                                          
    try:
        db = sqlite3.connect("library.db")
        mno=input("Enter Member Code :")
        mname=input("Enter Member Name :")
        mmobile=input("Enter Member Mobile No. :")
        print("Enter Date of Membership(Date,Month and Year seperately):") 
        DD=int(input("Enter Date :"))
        MM=int(input("Enter Month :"))
        YY=int(input("Enter Year :"))
        address=input("Enter Member Address :")
        Qry=("INSERT INTO member VALUES(?,?,?,?,?)")
        data=(mno,mname,mmobile,date(YY,MM,DD),address)
        db.execute(Qry,data)
        db.commit()
        db.close()                              
        print("Record Inserted Successfully.")
    except:
        print("Error (Insert Member).")
        db.close()
    x=input("Enter any key to continue...")

def deleteMember():
    try:
        db = sqlite3.connect("library.db")
        mno=input("Enter Member Code to be Deleted :")
        Qry=("DELETE FROM member WHERE mno=?")
        del_rec=(mno,)
        db.execute(Qry,del_rec)
        db.commit()
        db.close()                              
        print("Record(s) Deleted Successfully.")
    except:
        print("Error (Delete Member).")                          
        db.close()
    x=input("Enter any key to continue...")

def searchMember():
    try:
        db = sqlite3.connect("library.db")
        mname=input("Enter Member Name to be Searched :")
        query=("SELECT * FROM member where mname=?") 
        rec_srch=(mname,)
        Cursor = db.execute(query,rec_srch)
        Rec_count=0
        for (mno,mname,mmobile,mdom,address) in Cursor:
            print("========================================================")
            print("Member Code :",mno)
            print("Member Name :",mname)
            print("Mobile No.of Member :",mmobile)
            print("Date of Membership :",mdom)
            print("Address :",address)
            print("========================================================")
            Roc_count+=1
            if Rec_count%2==0:
                input("Press any key to continue...") 
                clrscreen()
        #print(Rec_count,"Record(S) found")
        db.commit()           
        db.close()                              
        print("Record(s) found.")
    except:
        print("Error (Search Members).")     
        db.close()
    x=input("Enter any key to continue...")

def updateMember():
    try:
        db = sqlite3.connect("library.db")
        mno=input("Enter Member Code of Member to be Updated :")                               
        rec_srch=(mno,)
        print("Enter New Data:")
        mname=input("Enter Member Name :")
        mmobile=input("Enter Mobile Number :")
        print("Enter Date of Membership(Date,Month and Year seperately:")         
        DD=int(input("Enter Date :"))
        MM=int(input("Enter Month :"))          
        YY=int(input("Enter Year :"))
        maddress=input("Enter Address :")
        Qry=("UPDATE member SET mname=?,mmobile=?,mdom=?,address=? WHERE mno=?")
        data=(mname,mmobile,date(YY,MM,DD),maddress,mno)
        db.execute(Qry,data)
        db.commit()
        db.close()
        print("Record(s) Updated Successfully.")
    except:
        print("Error (Member Update).")
        db.close()
    x=input("Enter any key to continue...")
