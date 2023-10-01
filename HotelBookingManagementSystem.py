import time
import random
import pickle
import os


def mainmenu() :
    print()
    print("\t"*8, "╔", "═"*24, "╗", sep='')
    print("\t"*8, "║","WELCOME TO HOTEL BOOKING", "║", sep='' )
    print("\t"*8, "╚", "═"*24,  "╝", sep='')
    print()
    
def tableofcontents():
    print("\t"*7,"═"*42) 
    print("\n","\t"*7, "             Table of Content")
    print("\t"*7,"═"*42)
    print()
    print("\t"*4 ,"1) Create a new record", "\t" * 5, "2) Updating Details ") 
    print("\t"*4 ,"3) Searching Records", "\t" * 6, "4) Displaying Records") #4 will have modification, deletion,payment, searching
    print("\t"*9 ,"5) Exit")
    print()
    print("─"*150)
    print()

    
    ch=int(input("Enter Your Choice ────>"))
    if ch== 1 :
        print("")
        start()
    elif ch == 2 :
        print("")
        update()
    elif ch == 3 :
        print("")
        search()
    elif ch == 4 :
        print("")
        display()
    elif ch == 5 :
        print("")
        exit()
    else :
        print("")
        print("You have entered an invalid key")
        tableofcontents()
        
        
        
        
def start():
    print()
    print("╔", "═"*15, "╗", sep='')
    print("║","BOOKING DETAILS","║",sep='')
    print("╚", "═"*15,  "╝", sep='')
    print()
    file=open("booking.dat","wb")
    name=input("NAME           :")
    phno=int(input("PHONE NUMBER   :"))
    add=input("ADDRESS        :")
    cid=input("CHECK-IN DATE  :")
    cod=input("CHECK-OUT DATE :")
    
    print()
    print("DETAILS HAVE BEEN SUCCESSFULLY ENTERED")
    print()
    print("Now showing the different Room Types, their Information and Prices. Please Wait.")
    print("\n"*2)
    time.sleep(2)
    
    #Room Info
    print()
    print("╔", "═"*22, "╗", sep='')
    print("║","HOTEL ROOM INFORMATION","║",sep='')
    print("╚", "═"*22,  "╝", sep='')
    print()
    print("╔", "═"*6, "╗", sep='')
    print("║","SINGLE" "║", sep='')
    print("╚", "═"*6,  "╝", sep='')
    print("A room assigned to one person.\n Will have one bed")
    print("─"*120)
    print()
    print("╔", "═"*6, "╗", sep='')
    print("║","DOUBLE" "║", sep='')
    print("╚", "═"*6,  "╝", sep='')
    print("A room assigned to two people. \n May have one or more beds.")
    print("─"*120)
    print()
    print("╔", "═"*6, "╗", sep='')
    print("║","TRIPLE" "║", sep='')
    print("╚", "═"*6,  "╝", sep='')
    print("A room that can accommodate three persons. \n It has been fitted with three twin beds, one double bed and one twin bed or two double beds.")
    print("─"*120)
    print()
    print("╔", "═"*5, "╗", sep='')
    print("║","QUEEN" "║", sep='')
    print("╚", "═"*5,  "╝", sep='')
    print("A room assigned to four people. \n May have two or more beds.")
    print("─"*120, "\n")
    print("╔", "═"*5, "╗", sep='')
    print("║","SUITE" "║", sep='')
    print("╚", "═"*5,  "╝", sep='')
    print("A parlour or living room connected with to one or more bedrooms.\n A room with one or more bedrooms and a separate living space.")
    print("─"*120, "\n")
    print()
    time.sleep(0.5)
    #Room Prices
    print()
    print("╔", "═"*17, "╗", sep='')
    print("║","HOTEL ROOM PRICES","║",sep='')
    print("╚", "═"*17,  "╝", sep='')
    print()
    print("1.Single", "────> 3500\n")
    print("2.Double", "────> 4500\n")
    print("3.Triple", "────> 5000\n")
    print("4.Queen", " ────> 5500\n")
    print("5.Suite", " ────> 6000\n")
    print()
    time.sleep(0.5)
    #Selecting The Room
    print("╔", "═"*16, "╗", sep='')
    print("║","HOTEL ROOM TYPES","║",sep='')
    print("╚", "═"*16,  "╝", sep='')
    print("\n"*1)
    print("1. Single\n")
    print("2. Double\n")
    print("3. Triple\n")
    print("4. Queen\n")
    print("5. Suite\n")
    qe=int(input("Enter your choice ────>"))
    print("\n"*2)
    if qe == 1 :
       room=("Single")
       print("ROOM CHOSEN   : SINGLE")
       price=("3500")
       print("PRICE         : 3500")
    elif qe == 2 :
        room=("Double")
        print("ROOM CHOSEN   : Double")
        price=("4500")
        print("PRICE         : 4500")
    elif qe == 3 :
        room=("Triple")
        print("ROOM CHOSEN   : TRIPLE")
        price=("5000")
        print("PRICE         : 5000")
    elif qe == 4 :
        room=("Queen")
        print("ROOM CHOSEN   : QUEEN")
        price=("5500")
        print("PRICE         : 5500")
    elif qe == 5 :
        room=("Suite")
        print("ROOM CHOSEN   : SUITE")
        price=("6000")
        print("PRICE         : 6000")
        
    
    rn=random.randrange(40)+500
    customerid=random.randrange(40)+150
    print()
    print("ROOM ALLOTTED :", rn)
    print("CUSTOMER ID   :", customerid)
    print()
    print("Please remember your Customer ID")
    record=[rn,customerid,name,phno,add,cid,cod,room,price]
    pickle.dump(record,file)
    record.clear()
    file.close()
    
    print()
    print("Returning back to main menu")
    print("Please wait.")
    time.sleep(2)
    tableofcontents()
    
    
#Updating Records
    
def update():
    print("╔", "═"*12, "╗", sep='')
    print("║","MODIFICATION" "║", sep='')
    print("╚", "═"*12,  "╝", sep='')
    try :
        file=open("booking.dat","rb")
        f=open("bookingd.dat","wb")
        l=pickle.load(file)
        print()
        w=int(input("Enter your Customer Id"))
        print()
        
        if l[1]==w:
            checkname=input("Do you want to change the name? (Enter y if yes)          :")
            print()
            if checkname.lower()=="y":
                cn=input("Enter Name :")
                print()
            else :
                cn=l[2]
            
            checkphno=input("Do you want to change your phone number? (Enter y if yes) :")
            print()
            if checkphno=="y":
                cpn=int(input("Enter Phone Number :"))
                print()
            else:
                cpn=l[3]
            
            checkadd=input("Do you want to change your adress? (Enter y if yes)       :")
            print()
            if checkadd=="y":
                ca=input("Enter Address :")
                print()
            else :
                ca=l[4]
        
        elif l[1]!= w :
            print("Record Not Found. Create one from the the main menu")
            tableofcontents()
            
        pickle.dump([l[0],l[1],cn,cpn,ca,l[5],l[6],l[7],l[8]],f)
        
    except EOFError :
        print("YOUR DETAILS HAVE BEEN SUCCESSFULLY UPDATED ")
        print()
        
    print()
    file.close()
    f.close()
    os.remove("booking.dat")
    os.rename("bookingd.dat","booking.dat")
    print("Returning back to the main menu....")
    time.sleep(1)
    tableofcontents()
            
    

#Searching Records
def search():
    print("╔", "═"*6, "╗", sep='')
    print("║","SEARCH" "║", sep='')
    print("╚", "═"*6,  "╝", sep='')
    f=open("booking.dat","rb")
    print()
    print("1. Via Customer ID")
    print("2. Via Name")
    print()
    t=int(input("Enter your Choice ────>"))
    print()
    if t==1:
        cuid=int(input("Enter The Customer ID :"))
        print()
        try :
            while True :
                data=pickle.load(f)
                
                if data[1]==cuid:
                    print("╔", "═"*147, "╗", sep='')
                    h=f"{'ROOM NUMBER':^15s}{'CUSTOMER ID':^15s}{'NAME':^15s}{'CONTACT NO.':^15s}{'ADDRESS':^15s}{'CHECK-IN DATE':^20s}{'CHECK-OUT DATE':^15s}{'ROOM':^15s}{'PRICE':^15s}"
                    print("║",h,"     ║")
                    print("╚", "═"*147,  "╝", sep='')
                    j=f"{data[0]:^15d}{data[1]:^15d}{data[2]:^15s}{data[3]:^15d}{data[4]:^15s}{data[5]:^20s}{data[6]:^15s}{data[7]:^15s}{data[8]:^15s}"
                    print("║",j,"     ║")
                    print("╚", "═"*147,  "╝", sep='')
                else :
                    print("Customer ID not found. This may be because a record has not been created. Create one from the main menu")
                    print("\n"*2)
                    time.sleep(1)
                    tableofcontents()
        except EOFError:
            print()
            print("SEARCH FINISHED")
            print()
            f.close()
            print("Returning back to the main menu....")
            print("Please Wait")
            time.sleep(1)
            tableofcontents()
    
    elif t==2:
        n=input("Enter your Name :")
        print()
        try:
            while True:
                data=pickle.load(f)
                if data[2].lower()==n.lower():
                    print("╔", "═"*147, "╗", sep='')
                    h=f"{'ROOM NUMBER':^15s}{'CUSTOMER ID':^15s}{'NAME':^15s}{'CONTACT NO.':^15s}{'ADDRESS':^15s}{'CHECK-IN DATE':^20s}{'CHECK-OUT DATE':^15s}{'ROOM':^15s}{'PRICE':^15s}"
                    print("║",h,"     ║")
                    print("╚", "═"*147,  "╝", sep='')
                    j=f"{data[0]:^15d}{data[1]:^15d}{data[2]:^15s}{data[3]:^15d}{data[4]:^15s}{data[5]:^20s}{data[6]:^15s}{data[7]:^15s}{data[8]:^15s}"
                    print("║",j,"     ║")
                    print("╚", "═"*147,  "╝", sep='')
                else :
                    print("Name not found. This may be because a record has not been created. Create one from the main menu")
                    print("\n"*2)
                    time.sleep(1)
                    tableofcontents()

        except EOFError:
            print()
            print("SEARCH FINISHED")
            print()
            f.close()
            print("Returning back to the main menu....")
            print("Please Wait")
            time.sleep(1)
            tableofcontents()



def display():
    f=open("booking.dat","rb")
    print("╔", "═"*7, "╗", sep='')
    print("║","DISPLAY" "║", sep='')
    print("╚", "═"*7,  "╝", sep='')
    print()
    try:
        while True:
            data=pickle.load(f)
            print("╔", "═"*147, "╗", sep='')
            h=f"{'ROOM NUMBER':^15s}{'CUSTOMER ID':^15s}{'NAME':^15s}{'CONTACT NO.':^15s}{'ADDRESS':^15s}{'CHECK-IN DATE':^20s}{'CHECK-OUT DATE':^15s}{'ROOM':^15s}{'PRICE':^15s}"
            print("║",h,"     ║")
            print("╚", "═"*147,  "╝", sep='')
            j=f"{data[0]:^15d}{data[1]:^15d}{data[2]:^15s}{data[3]:^15d}{data[4]:^15s}{data[5]:^20s}{data[6]:^15s}{data[7]:^15s}{data[8]:^15s}"
            print("║",j,"     ║")
            print("╚", "═"*147,  "╝", sep='')
    except EOFError:
        print()
        print("DISPLAY FINISHED")
        print()
        f.close()
        
    e=input("Do you want to return back to the main menu?")
    print()
    if e=="y":
        print("Returning back to the main menu....")
        print("Please Wait")
        time.sleep(1)
        tableofcontents()
    else :
        print("Exiting the program")
        exit()

#Main
mainmenu()
tableofcontents()
