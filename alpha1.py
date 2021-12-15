print("""

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▄▀ ░░█ █▀█   █▀▀ █▀█ █▀█ █▀▀ █▀▀ █▀█ █▄█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █░█ █▄█ █▀▄   █▄█ █▀▄ █▄█ █▄▄ ██▄ █▀▄ ░█░
""")

#admin login
while True:
    password="grocery"
    username=input("please enter your username:  ")

    if username != "":
        pw=input("please enter you password:   ")
        if pw==password:
            print("\n\n\n.............................................LOGIN SUCCESSFUL.............................................")
            

            #menu        
            print("please choose a feature")
            ifs=True
            while ifs:
                print("""
                1. Add items to the store 
                2. Remove items from the store
                3. Modify item price
                4. Check availability of an item for the store
                5. Admin login credentials
                6. Customer bill generation
                7. View available stock
                8. Exit programme""")
                
                x=input("\n what would you like to do ? :  ")
                if x=="1":
                    a = input('pls input veg name: ')
                    b = int(input("pls input price: "))
                    c = int(input("pls input qty: "))
                    additem(a,c,b,maindb)
                    print("\n item added")
                    print(maindb)




                # item removal
                elif x=="2":
                    print("these are the items currently in stock :")
                    for i in maindb:
                        print(i,maindb[i])
                    remove=input("what item(s) would you want to remove? : ")
                    if remove in maindb:
                        del maindb[remove]
                        print(maindb)
                        print("item successfully removed")
                    else:
                        print("this item does not exist, please try again.")





                # item modification
                elif x=="3":
                    print("\n price modified")

                #item availability    
                elif x=="4":
                    print("\n item unavailable")
                #login successful    

                #create a bill
                elif x=="6":
                    print("\n bill generation")
                    custname=input("please enter your name: ")
                    custno=int(input("please enter your phone number:"))
                    
                   




                #check for availability of an item
                elif x=="7":
                    print("\nStock availability :")

                    import csv
                    reader=csv.reader(open("veg.csv","r"))
                    data=[]
                    for row in reader:
                        data.append(row)
                    ##print(data)

                    header=data.pop(0)
                    def textalign(text,length):
                        if len(text)>length:
                            text=text[:length]
                        elif len(text)<length:
                            text=(text+" "*length)[:length]
                        return text 
                    print("#"*71)
                    print("# ", end=" ")
                    for x in header:
                        print(textalign(x,20),end=" # ")
                    print()
                    print("#"*71)

                    for row in data:
                        print("# ",end=" ")
                        for column in row:
                            print(textalign(column,20),end=" # ")
                        print()

