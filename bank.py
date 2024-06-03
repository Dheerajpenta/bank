def import_and_create_bank(filename):
    bank = {}
    
    with open(filename, 'r') as file:
        lines = file.readlines();
        
        for line in lines:
            data = line.split(':');
            if len(data) != 2:
                continue
            key = data[0].strip()
            value = data[1].strip()
            try:
                bank[key] = bank.get(key, 0) + float(value)
            except ValueError:
                bank[key] = bank.get(key, 0)
    return bank

def signup(user_accounts, log_in, username, password):
    if user_accounts.get(username, False) or username == password:
        return False;
    if validatePassword(password):
        user_accounts[username] = password;
        log_in[username] = False;
        return True;
    return False;

def validatePassword(password):
    if len(password) < 8:
        return False
    lower = False
    upper = False
    digit = False
    for char in password:
        if char.islower():
            lower = True
            continue
        elif char.isupper():
            upper = True
            continue
        elif char.isdigit():
            digit = True
            continue
    if(lower and upper and digit):
        return True
    return False

def import_and_create_accounts(filename):
    user_accounts = {}
    log_in = {}

    with open(filename, 'r') as file:
        lines = file.readlines();

        for line in lines:
            data = line.split('-');
            if len(data) != 2:
                continue;

            username = data[0].strip();
            password = data[1].strip();

            if user_accounts.get(username, False):
                continue;
            if not validatePassword(password):
                continue;

            user_accounts[username] = password;
            log_in[username] = False;

    return user_accounts,log_in;

def login(user_accounts, log_in, username, password):
    if user_accounts.get(username, False) and user_accounts.get(username) == password:
        log_in[username] = True
        return True
    return False

def update(bank, log_in, username, amount):
    if log_in.get(username, 'False'):
        if bank.get(username, 0) + amount < 0:
            return False;
        bank[username] = bank.get(username, 0) + amount;
        return True;
    return False;

def transfer(bank, log_in, userA, userB, amount):
    if userA in log_in and log_in.get(userA, False) and userB in log_in:
        if bank.get(userA, 0) - amount < 0:
            return False;
        if bank.get(userB, 0) + amount < 0:
            return False;
        bank[userA] = bank.get(userA, 0) - amount;
        bank[userB] = bank.get(userB, 0) + amount;
        return True;
    return False;

def change_password(user_accounts, log_in, username, old_password, new_password):
    if user_accounts.get(username, False) and log_in.get(username, False):
        if user_accounts.get(username, '') != old_password:
            return False;
        if user_accounts.get(username, '') == new_password:
            return False;
        if validatePassword(new_password):
            user_accounts[username] = new_password;
            return True;
        return False;
    return False;

def delete_account(user_accounts, log_in, bank, username, password):
    if user_accounts.get(username, False) and log_in.get(username, False) and user_accounts.get(username, '') == password:
        del user_accounts[username];
        del log_in[username];
        del bank[username];
        return True;
    return False;

def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()
