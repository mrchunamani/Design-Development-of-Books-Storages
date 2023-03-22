#PYTHON MODULE:MENULIB
import Book
import Member
import Issue

def menuBook():
    while True:
        #Book.clrscreen()
        print("========================================================")
        print("\t\t Book Record Management\n")
        print("========================================================")
        print("1.Add Book Record")
        print("2.Display Book Records")
        print("3.Search Book Record")
        print("4.Delete Book Record")
        print("5.Update Book Record")
        print("6.Back to Main Menu")
        print("========================================================")
        choice=int(input("Enter Your Choice (1 to 6) :"))
        if choice==1:
            Book.insertData()
        elif choice==2:
            Book.display()
        elif choice==3:
            Book.searchBookRec()
        elif choice==4:
            Book.deleteBook()
        elif choice==5:
            Book.updateBook()
        elif choice==6:
            return
        else:
            print("Wrong Choice.....Enter Your Choice Again")
    x=input("Enter any key to continue...")

def menuMember():
    while True:
        #Book.clrscreen()
        print("========================================================")
        print("\t\t Member Management\n")
        print("========================================================")
        print("1.Add Member Record")
        print("2.Display Member Records")
        print("3.Search Member Record")
        print("4.Delete Member Record")
        print("5.Update Book Record")
        print("6.Back to Main Menu")
        print("========================================================")
        choice=int(input("Enter Your Choice (1 to 6) :"))
        if choice==1:
            Member.insertMember()
        elif choice==2:
            Member.display()
        elif choice==3:
            Member.searchMember()
        elif choice==4:
            Member.deleteMember()
        elif choice==5:
            print("No such Function")
            # Member.updateMember()
        elif choice==6:
            return
        else:
            print("Wrong Choice.....Enter Your Choice Again.")
    x=input("Enter any key to continue...")

def menuIssueReturn():
    while True:
        #Book.clrscreen()
        print("========================================================")
        print("\t\t Book Issue/Return Management\n")
        print("========================================================")
        print("1.Issue Book")
        print("2.Display Issued Book Records")
        print("3.Return Issued Book")
        print("4.Back to Main Menu")
        print("========================================================")
        choice=int(input("Enter Your Choice (1 to 4) :"))
        if choice==1:
            Issue.issueBook()
        elif choice==2:
            Issue.showIssuedBooks()
        elif choice==3:
            Issue.returnBook()
        elif choice==4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice Aain")
    x=input("Enter any key to continue...")


            
