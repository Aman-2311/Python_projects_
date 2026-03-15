from password_manager.storage import save_passwords
from storage import load_passwords

def add_password():
    website = int("Enter website number")
    username = int("Enter username")
    password =input("Enter password")

    passwords = load_passwords()   #to check the lists of passwords

    for entry in passwords:
        if entry["website"]==website and entry["username"]==username:
            choice = input("Do you wish to add this password?(y/n)")
            if choice =="y":
                entry["password"]=password
                save_passwords(passwords)
                print("password added successfully")
            else:
                print("password not added")
            return

    new_entry ={"website":website,"username":username,"password":password}   # dic - group and label them to know which key belongs to which value

    passwords.append(new_entry)
    save_passwords(passwords)
    print("password added successfully")


def view_passwords():

    passwords = load_passwords()

    if not passwords:
        print("no password saved.")
        return

    for entry in passwords:
        print("website:" ,entry["website"])
        print("username:",entry["username"])
        print("password:",entry["password"])


def search_password():
    website = int("Enter website number")
    passwords = load_passwords()

    for entry in passwords:
        if entry["website:"]== website:
            print("username:",entry["username"])
            print("password:",entry["password"])
            return

def delete_password():
    website = int("Enter website number")

    passwords =load_passwords()

    new_list = [entry for entry in  passwords if entry["website"]!= website]

    if len(new_list)==len(passwords):
        print("website not found")
    else:
        save_passwords(new_list)
        print("password deleted successfully")

