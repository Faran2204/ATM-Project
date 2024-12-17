from cardholder import cardholder
def print_menu():
    ###options to print
    print("please choose from one of the following options")
    print("1, Deposit")
    print("2, Withdraw")
    print("3, Show Balance")
    print("4, Exit")

def deposit(cardholder):
    try:
        deposit = float(input("how much money would you like to deposit: "))
        cardholder.set_balance(cardholder.get_balance() + deposit)
        print("thnx for depositing money. your new balance is: ", str(cardholder.get_balance()))

    except:
        print("invalid input")

def Withdraw(cardHolder):
    try:
        withdraw = float(input("How much mone would you like to withdraw: "))
        ###check availability
        if(cardHolder.get_balance() < withdraw):
            print("Insufficent funds")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("you're good to go thank u")
    except:
        print("invalid input")

def check_balance(cardHolder):
    print("ur current balance is; ",cardHolder.get_balance())


if __name__ == "__main__":
    current_user = cardholder("", "", "", "", "", )
    ###create repo
list_of_cardHolders = []
list_of_cardHolders.append(cardholder("1234567897654321", 1234, "faran", "ahmad", 345.66))
list_of_cardHolders.append(cardholder("1234567897654331", 1234, "aafaq", "ahmad", 355.66))
list_of_cardHolders.append(cardholder("1234567897654341", 1234, "zohaib", "ahmad", 348.66))
list_of_cardHolders.append(cardholder("1234567897654351", 1234, "faraz", "ahmad", 385.66))
list_of_cardHolders.append(cardholder("1234567897654361", 1234, "bily", "ahmad", 345.66))

###prompt user for card number
debitCardNum = ""
while True:
    try:
        debitCardNum = input("please isert ur debit card: ")
        debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
        if(len(debitMatch) > 0):
            current_user = debitMatch[0]
            break
        else:
             print("Card number not recognised. please try again")
    except:
        print("Card number not recognised. please try again")

    ### prompt pin
    while True:
        try:
            userPin = int(input("please enter user pin: ").strip)
            if(current_user.get_pin() == userPin):
                break
            else:
                print("invalid pin. try again")
        except:
            print("invalid pin. try again")

###print options
print("welcome ", current_user.get_firstname(),":")
option = 0
while (True):
    print_menu()
    try:
        option = int(input())
    except:
        print("invalid input. try again")

    if(option == 1):
        deposit(current_user)
    elif(option == 2):
        Withdraw(current_user)
    elif(option == 3):
        check_balance(current_user)
    elif(option == 4):
        break
    else:
        option = 0

print("Thank you have a good day")