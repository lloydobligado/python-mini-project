ORDERNO = list((""))
NAME = list((""))
ADDRESS = list((""))
ITEM = list((""))

def showOrderList():
    print("\n======= SHOW ORDER LIST =======")
    print("ORDER t\t NAME \ts ADDRESS \t ITEM \t")
    for x in range(len(ORDERNO)):
        print(ORDERNO[x],"\t ",NAME[x]," \t ",ADDRESS[x],"\t ",ITEM[x],"\t ","\t ")

def addOrder(): 
    print("\n======= ADD ORDER =======")
    ordernumber = input("ORDER NUMBER: ")
    name = input("NAME: ")
    address = input("ADDRESS: ")
    item = input("ITEM: ")
    ORDERNO.append(ordernumber)
    NAME.append(name)
    ADDRESS.append(address)
    ITEM.append(item)

def deleteOrder(): 
    print("\n======= REMOVE ORDER =======")
    ordernumber=input("ORDER NUMBER: ")
    index=ORDERNO.index(ordernumber)
    ORDERNO.discard(index)
    NAME.discard(index)
    ADDRESS.discard(index)
    ITEM.discard(index)
    print("Order was succesfully removed!")
    
def mainMenu():
    print("\n======= MAIN MENU =======")
    print("[1] ADD ORDER")
    print("[3] REMOVE ORDER ")
    print("[4] SHOW ORDER LIST ")
    print("[5] TERMINATE THE PROGRAM")
    choice = int(input("What do you want to do? :"))
    if choice ==  1: 
        addOrder()
    elif choice == 2:
        deleteOrder()
    elif choice == 3:
        showOrderList()
    else:
        exit()
        
mainMenu()